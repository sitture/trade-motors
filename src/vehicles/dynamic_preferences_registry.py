from dynamic_preferences.types import StringPreference
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
