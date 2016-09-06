"""
app url link
"""
from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from .forms import BootstrapAuthenticationForm
from .views import blocking
from .views import blocked
from .views import IndexPage

urlpatterns = [
    url(r'^$', view=IndexPage.as_view(), name='home'),
    url(r'^blocking/$', view=blocking, name='blocking'),
    url(r'^blocked/$', view=blocked, name='blocked'),
    url(r'^login/$',
        login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
        },
        name='login'),
    url(r'^logout$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),
]
