from django.test import TestCase
from django.core.urlresolvers import reverse
from vehicles.models import Category, VehicleMake, Vehicle


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
        self.test_make_one = VehicleMake.objects.create(
            v_make='Alfa Romeo',
            slug='alfa-test'
        )
        self.vehicle = Vehicle.objects.create(
            category=self.main_category,
            make=self.test_make_one,
            model='Test',
            desc='Test Vehicle One',
            slug = 'test-vehicle-slug'
        )
        self.vehicle_url = reverse(
            'vehicle', args=[
                self.main_category.slug,
                self.vehicle.pk,
                self.vehicle.slug
            ]
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
    
    def test_vehicle_page(self):
        self.assertEquals(
            '/category/main/detail/1/test-vehicle-slug',
            self.vehicle_url
        )
        response = self.client.get(self.vehicle_url)
        self.assertEquals(
            200, response.status_code
        )