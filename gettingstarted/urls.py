from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path, reverse
from django.conf.urls import include, url
from django.views.generic import TemplateView

from django.contrib import admin
from django.contrib.auth.views import LogoutView
admin.autodiscover()


import hello.views
import carts.urls
import products.urls
import accounts.views
import towguideline.views

from accounts.views import login_page, register_page

app_name = products

urlpatterns = [
    url(r'^$', hello.views.home_page, name='home_url'),
    url(r'^about_page/$', hello.views.about_page, name= 'about_page'),
    url(r'^contact/$', hello.views.contact_page, name='contact_url'),
    url(r'^login/$', accounts.views.login_page, name= 'login'),
    url(r'^logout/$', LogoutView.as_view(), name= 'logout'),
    url(r'^cart/', include(('carts.urls', 'cart'))),
    url(r'^search/', include(('search.urls', 'search'))),
    url(r'^products/', include(('products.urls', 'products'))),
    url(r'^register/$', accounts.views.register_page, name='register'),
    url(r'^register/guest/$', accounts.views.guest_register_view, name='guest_register'),
    url(r'^estimator/$', towguideline.views.TowEstimatorView, name= 'Tow_Estimator_View'),
    url(r'^admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
