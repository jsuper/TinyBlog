from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TinyBlog.views.home', name='home'),
    # url(r'^TinyBlog/', include('TinyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^create/$', views.new_post, name='new_post'),
)
