import django_cas_ng.views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    # path('logout/', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    path('logout/', views.MyLogoutView.as_view(), name='cas_ng_logout'),
    path('callback/', django_cas_ng.views.CallbackView.as_view(), name='cas_ng_proxy_callback'),
    path('sync-users/', views.sync_users, name='sync_users')
]
