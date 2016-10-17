"""
Definition of urls for mydd.
"""

from datetime import datetime
from django.conf.urls import url
from app.forms import BootstrapAuthenticationForm
from app.views import home, contact, about
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about', about, name='about'),
    url(r'^login/$',
        login, {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context': {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        logout, {
            'next_page': '/',
        },
        name='logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
