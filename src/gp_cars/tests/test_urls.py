from django.test import TestCase
from django.core.urlresolvers import reverse
from vehicles.models import Category, VehicleMake, Vehicle
from vehicles.context_processor import ContactDetail, Social


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
            slug='test-vehicle-slug'
        )
        self.vehicle_url = reverse(
            'vehicle', args=[
                self.main_category.slug,
                self.vehicle.pk,
                self.vehicle.slug
            ]
        )

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(
            response.status_code, 200
        )
        response.status_code == 200

    def test_basepage_contains_all_categories_list(self):
        response = self.client.get(reverse('home'))
        expected_categories = \
            Category.objects.get_categories_with_sub_categories()
        actual_categories = response.context[-1]['all_categories']
        self.assertEquals(
            actual_categories,
            expected_categories
        )

    def test_basepage_contains_contact_details(self):
        response = self.client.get(reverse('home'))
        expected_contact_details = \
            ContactDetail.objects.get_latest_contact_details()
        actual_contact_details = \
            response.context[-1]['contact_details']
        self.assertEquals(
            actual_contact_details,
            expected_contact_details
        )

    def test_basepage_contains_social_providers(self):
        response = self.client.get(reverse('home'))
        expected_social_providers = \
            list(Social.objects.all())
        actual_social_providers = \
            response.context[-1]['social_providers']
        self.assertEquals(
            actual_social_providers,
            expected_social_providers
        )

    def test_about_us_page(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, 200
        )
        self.assertEquals(
            url, '/about-us'
        )

    def test_exports_page(self):
        url = reverse('exports')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, 200
        )
        self.assertEquals(
            url, '/exports'
        )

    def test_how_to_buy_page(self):
        url = reverse('how_to_buy')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, 200
        )
        self.assertEquals(
            url, '/how-to-buy'
        )

    def test_contact_us_page(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, 200
        )
        self.assertEquals(
            url, '/contact-us'
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
