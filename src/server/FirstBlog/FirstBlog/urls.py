"""FirstBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from Data import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^Data/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'Data.views.home', name='home'),
    url(r'^home/', 'Data.views.home', name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^form_upload.html$',
        'Data.views.post_form_upload', name='post_form_upload'),
    url(r'^create/', 'Data.views.post_form_upload', name='post_form_upload'),
    url(r'^about/', 'Data.views.about', name='about'),
    url(r'^clear/', 'Data.views.clear', name='clear'),
]
