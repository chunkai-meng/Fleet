"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from .routers import router

debug_paths = [
    path('api/docs/', include_docs_urls(title='Fleet Django Backend', public=False)),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api/admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls'), name='accounts'),
]

if settings.DEBUG is True:
    urlpatterns += debug_paths

admin.site.site_url = '/api/docs/'
admin.site.site_header = 'Fleet Booking System'
