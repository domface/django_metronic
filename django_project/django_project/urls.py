from django.conf.urls import patterns, include, url
from Romulus.views import MetronicAdmin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^Romulus/', include('Romulus.urls')),
    #url(r'^test', 'Romulus.views.test'),
    url(r'^$', 'Romulus.views.index'),

    url(r'^json_test', 'Romulus.views.json_test'),
    url(r'^login_test', 'Romulus.views.login_test'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', MetronicAdmin.as_view(), name='metronicadmin'),
)
