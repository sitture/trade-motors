from django.test import TestCase
from vehicles import context_processor
from vehicles.models import Category


class ContextProcessorTest(TestCase):

    def test_get_all_categories_in_a_list(self):
        # setup data for test
        main_category = Category.objects.create(
            category_name='Main Category',
            slug='main-category'
        )
        sub_category = Category.objects.create(
            category_parent=main_category,
            category_name='Sub Category',
            slug='sub-category'
        )
        expected_result = [[main_category, [sub_category]]]
        # get the actual data
        categories = list(Category.objects.filter(category_parent=None))
        sub_categories = list(Category.objects.exclude(category_parent=None))
        actual_result = context_processor.get_all_categories(
            categories, sub_categories)

        self.assertEquals(
            expected_result, actual_result
        )
