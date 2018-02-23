from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.home_page, name='home_page'),
    url(r'^about_page/$', hello.views.about_page, name= 'about_page'),
    url(r'^contact/$', hello.views.contact_page, name= 'contact_page'),
    url(r'^login/$', hello.views.login_page, name= 'login'),
    url(r'^register/$', hello.views.register_page, name= 'register_page'),
    path('admin/', admin.site.urls),
]
