from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from vehicles.views import home_page, category_page, \
    vehicle_detail_page, exports_page, contact_page
# The ugettext_lazy function is used to mark the language names for translation
from django.utils.translation import ugettext_lazy as _
from dynamic_preferences import global_preferences_registry


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

# change the header title on admin
# instanciate a manager for global preferences
global_preferences = global_preferences_registry.manager()
admin.site.site_header = _(global_preferences['general__admin_header'])
admin.site.site_title = _(global_preferences['general__admin_title'])

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
