from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from TinyBlog import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index),
    # url(r'^TinyBlog/', include('TinyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/',include('users.urls', namespace='users')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
)




