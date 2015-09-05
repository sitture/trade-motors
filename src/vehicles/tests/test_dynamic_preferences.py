from django.test import TestCase
from dynamic_preferences import global_preferences_registry
from django.conf import settings


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

    def test_number_of_vehicles_on_homepage_preference(self):
        self.assertEquals(
            self.global_preferences['homepage__number_of_vehicles'],
            16
        )

    def test_default_email_address_preference(self):
        self.assertEquals(
            self.global_preferences['general__default_email'],
            settings.DEFAULT_EMAIL_ADDRESS
        )
