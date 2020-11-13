import requests
import json
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from django_cas_ng.views import LogoutView
from django_cas_ng.signals import cas_user_logout
from django_cas_ng.models import SessionTicket, ProxyGrantingTicket
from django_cas_ng.utils import get_protocol, get_cas_client
from django.contrib.auth import logout as auth_logout
from urllib import parse as urllib_parse
from .models import UserProfile
from api_key.utils import sign_request
from api_key.models import ApiKey


class MyLogoutView(LogoutView):
    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Redirects to CAS logout page

        :param request:
        :return:
        """
        # next_page = clean_next_page(request, request.GET.get('next'))
        next_page = request.GET.get('next', '')
        # try to find the ticket matching current session for logout signal
        try:
            st = SessionTicket.objects.get(session_key=request.session.session_key)
            ticket = st.ticket
        except SessionTicket.DoesNotExist:
            ticket = None
        # send logout signal
        cas_user_logout.send(
            sender="manual",
            user=request.user,
            session=request.session,
            ticket=ticket,
        )
        # clean current session ProxyGrantingTicket and SessionTicket
        ProxyGrantingTicket.objects.filter(session_key=request.session.session_key).delete()
        SessionTicket.objects.filter(session_key=request.session.session_key).delete()
        auth_logout(request)

        if settings.CAS_LOGOUT_COMPLETELY:
            # protocol = get_protocol(request)
            force_ssl = getattr(settings, 'CAS_FORCE_SSL_SERVICE_URL', False)
            protocol = 'https' if force_ssl else get_protocol(request)
            # host = request.get_host()
            host = request.get_host().split(':')[0]
            redirect_url = urllib_parse.urlunparse(
                (protocol, host, next_page, '', '', ''),
            )
            client = get_cas_client(request=request)
            # print("protocol: {} host: {} redirect_url: {} client: {}".format(
            #     protocol, host, redirect_url, client
            # ))
            return HttpResponseRedirect(client.get_logout_url(redirect_url))

        return HttpResponseRedirect(next_page)


def sync_users(request):
    # code, message, data = get_and_sync()
    api_key = hasattr(settings, 'API_KEY_CAS') and settings.API_KEY_CAS
    updated_count = 0
    created_count = 0
    created_users = []

    url = settings.CAS_SERVER_URL + 'user-list/?api_key={}'.format(api_key)
    try:
        key = ApiKey.objects.get(api_key=api_key)
    except ApiKey.DoesNotExist:
        return JsonResponse({'message': 'api_key not found', 'code': 0, 'data': []})

    url = sign_request(url, key.api_secret)
    response = requests.get(url, verify=False)
    code, content = response.status_code, response.content
    if code == 200:
        data = response.json()['data']
        for d in data:
            obj, created = UserProfile.objects.update_or_create(username=d['username'], defaults=d)
            if created:
                created_count += 1
                created_users.append(obj.username)
            else:
                updated_count += 1

        message, code, data = 'checked {} users, {} user updated, {} users created: {}'.format(
            len(data), updated_count, created_count, created_users), 1, []
    else:
        message, code, data = json.loads(content.decode('utf-8')).get('detail', 'error'), 0, []

    return JsonResponse({'message': message, 'code': code, 'data': []})
