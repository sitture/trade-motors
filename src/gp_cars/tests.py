from django.test import TestCase


class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_us_page(self):
        response = self.client.get('/about-us')
        self.assertEqual(response.status_code, 200)

    def test_contact_us_page(self):
        response = self.client.get('/contact-us')
        self.assertEqual(response.status_code, 200)
