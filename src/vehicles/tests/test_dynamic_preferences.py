from django.test import TestCase
from dynamic_preferences import global_preferences_registry


class DynamicPreferencesTests(TestCase):

    def setUp(self):
        # instanciate a manager for global preferences
        self.global_preferences = global_preferences_registry.manager()

    def test_admin_site_title_preference(self):
        self.assertEquals(
            self.global_preferences['general__admin_title'],
            'Global Trade Motors'
        )

    def test_admin_site_header_preference(self):
        self.assertEquals(
            self.global_preferences['general__admin_header'],
            'Global Trade Motors'
        )
