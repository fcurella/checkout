from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from payments import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'checkout.views.home', name='home'),
    # url(r'^checkout/', include('checkout.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', views.PaymentList.as_view(), name='payment_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^payments/(?P<pk>\d+)/$', views.PaymentDetail.as_view(), name='payment_detail'),
    url(r'^payments/create/$', views.PaymentCreate.as_view(), name='payment_create'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="accounts_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name="accounts_logout"),
)

urlpatterns += staticfiles_urlpatterns()
