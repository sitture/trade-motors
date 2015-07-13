from django.test import TestCase
# import the models to test
from vehicles.models import Category, VehicleMake

class CategoryModelTest(TestCase):
    
    def test_str_with_category_parent(self):
        parent = 'Parent'
        child = 'Child'
        parent_category = Category.objects.create(
            category_name=parent
        )
        child_category = Category(
            category_parent=parent_category,
            category_name=child
        )
        
        expected_result = '{0} ({1})'.format(child, parent)
        
        self.assertEquals(
            str(child_category),
            expected_result
        )
    
    def test_str_with_no_category_parent(self):
        category_test_name = 'Test'
        category = Category(category_name=category_test_name)
        self.assertEquals(
            str(category),
            category_test_name
        )
        
    def test_verbose_name(self):
        self.assertEquals(
            str(Category._meta.verbose_name),
            'Category'
        )
        
    def test_verbose_name_plural(self):
        self.assertEquals(
            str(Category._meta.verbose_name_plural),
            'Categories'
        )


class VehicleMakeModelTest(TestCase):
    
    def test_str_representation(self):
        make_name = 'Toyota'
        vehicle_make = VehicleMake(v_make=make_name)
        self.assertEquals(
            str(vehicle_make),
            make_name
        )
    
    def test_verbose_name(self):
        self.assertEquals(
            str(VehicleMake._meta.verbose_name),
            'Make'
        )
        
    def test_verbose_name_plural(self):
        self.assertEquals(
            str(VehicleMake._meta.verbose_name_plural),
            'Makes'
        )
    
    
    