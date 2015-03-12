from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfirstsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #
    # url(regex,view)

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'trips.views.hello_world'),
    url(r'^hello_html/$', 'trips.views.hello_html'),
    url(r'^hello_temp/$', 'trips.views.hello_temp'),
    url(r'^$','trips.views.home'), # direct to home
)
