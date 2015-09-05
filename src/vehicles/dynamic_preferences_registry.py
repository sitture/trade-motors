from dynamic_preferences.types import StringPreference, \
    IntegerPreference
from dynamic_preferences import global_preferences_registry


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
