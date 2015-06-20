from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField('Name', max_length=50, blank=False, null=False)
    category_image = models.ImageField('Image', upload_to='category_images')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.category_name)
    

class CategoryType(models.Model):
    category = models.ForeignKey(Category)
    category_type = models.CharField('Type', max_length=50, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return str(self.category_type)
    

class VehicleMake(models.Model):
    v_make = models.CharField('Make', max_length=50, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return str(self.v_make)


class Vehicle(models.Model):
    v_category = models.ForeignKey(Category)
    v_category_type = models.ForeignKey(CategoryType)
    v_make = models.ForeignKey(VehicleMake)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return str(self)
    

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    v_image = models.ImageField('Image', upload_to='vehicle_images')
    
    def __unicode__(self):
        return '%s\'s Image' % self.vehicle