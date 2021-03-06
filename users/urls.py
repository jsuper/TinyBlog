from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from users import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TinyBlog.views.home', name='home'),
    # url(r'^TinyBlog/', include('TinyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^create/$', views.create, name = 'create'),
    url(r'^login/$', views.login, name = 'login'),
)
