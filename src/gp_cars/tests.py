from django.test import TestCase
from django.core.urlresolvers import reverse
from vehicles.models import Category


class ProjectTests(TestCase):
    
    def setUp(self):
        self.main_category = Category.objects.create(
            category_name='Main Category',
            slug='main',
            show_on_home_page=False
        )
        self.category_url = reverse(
            'category', args=[self.main_category.slug]
        )

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(
            response.status_code, 200
        )

    def test_about_us_page(self):
        response = self.client.get('/about-us')
        self.assertEqual(
            response.status_code, 200
        )

    def test_contact_us_page(self):
        response = self.client.get('/contact-us')
        self.assertEqual(
            response.status_code, 200
        )
    
    def test_robots_txt_page(self):
        response = self.client.get('/robots.txt')
        self.assertEquals(
            response.status_code, 200
        )
    
    def test_category_page(self):
        self.assertEquals(
            '/category/main/', self.category_url
        )
        response = self.client.get(self.category_url)
        self.assertEquals(
            200, response.status_code
        )