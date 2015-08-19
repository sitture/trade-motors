"""gp_cars URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from vehicles.views import home_page, category_page, \
    vehicle_detail_page, contact_page, exports_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about-us$', home_page, name='about'),
    url(r'^exports$', exports_page, name='exports'),
    url(r'^contact-us$', contact_page, name='contact'),
    url(r'^category/(?P<slug>[-a-zA-Z0-9]+)/$',
        category_page, name='category'),
    url(r'^category/(?P<category_slug>[-a-zA-Z0-9]+)/detail/(?P<vehicle_id>\d+)/(?P<vehicle_slug>[-a-zA-Z0-9]+)$',
        vehicle_detail_page,
        name='vehicle'
        ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^robots\.txt$',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain')
        ),
]

SITE_HEADER_TITLE = 'Global Trade Motors'

# change the header title on admin
admin.site.site_header = SITE_HEADER_TITLE
admin.site.site_title = SITE_HEADER_TITLE

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
