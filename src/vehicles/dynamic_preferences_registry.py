from dynamic_preferences.types import StringPreference, \
    IntegerPreference, BooleanPreference
from dynamic_preferences.registries import global_preferences_registry
from django.conf import settings


@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = 'general'
    name = 'admin_title'
    verbose_name = 'Admin Site Title'
    default = 'Global Trade Motors'


@global_preferences_registry.register
class SiteHeader(StringPreference):
    section = 'general'
    name = 'admin_header'
    verbose_name = 'Admin Site Header'
    default = 'Global Trade Motors'


@global_preferences_registry.register
class NumberOfVehiclesOnHompage(IntegerPreference):
    section = 'homepage'
    name = 'number_of_vehicles'
    verbose_name = 'Homepage Vehicles'
    help_text = 'Please enter the number of vehicles to show on homepage.'
    default = 16


@global_preferences_registry.register
class DefaultEmailAddress(StringPreference):
    section = 'general'
    name = 'default_email'
    verbose_name = 'Default Email Address'
    help_text = 'Please enter the email address to show on the top header \
                 and other pages.'
    default = 'info@globaltrademotors.com'
    if settings.DEFAULT_EMAIL_ADDRESS:
        default = settings.DEFAULT_EMAIL_ADDRESS


@global_preferences_registry.register
class LiveChatFeature(BooleanPreference):
    section = 'general'
    name = 'live_chat'
    verbose_name = 'Live Chat'
    help_text = 'Turn Live Chat feature on/off.'
    default = False
