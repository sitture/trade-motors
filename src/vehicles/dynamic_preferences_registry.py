from dynamic_preferences.types import StringPreference, IntegerPreference, BooleanPreference, Section
from dynamic_preferences.registries import global_preferences_registry
from django.conf import settings


general_section = Section('general')
homepage_section = Section('homepage')


@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = general_section
    name = 'admin_title'
    verbose_name = 'Admin Site Title'
    default = 'Global Trade Motors'


@global_preferences_registry.register
class SiteHeader(StringPreference):
    section = general_section
    name = 'admin_header'
    verbose_name = 'Admin Site Header'
    default = 'Global Trade Motors'


@global_preferences_registry.register
class NumberOfVehiclesOnHompage(IntegerPreference):
    section = homepage_section
    name = 'number_of_vehicles'
    verbose_name = 'Homepage Vehicles'
    help_text = 'Please enter the number of vehicles to show on homepage.'
    default = 16


@global_preferences_registry.register
class DefaultEmailAddress(StringPreference):
    section = general_section
    name = 'default_email'
    verbose_name = 'Default Email Address'
    help_text = 'Please enter the email address to show on the top header \
                 and other pages.'
    default = 'info@globaltrademotors.com'
    if settings.DEFAULT_EMAIL_ADDRESS:
        default = settings.DEFAULT_EMAIL_ADDRESS


@global_preferences_registry.register
class LiveChatFeature(BooleanPreference):
    section = general_section
    name = 'live_chat'
    verbose_name = 'Live Chat'
    help_text = 'Turn Live Chat feature on/off.'
    default = False
