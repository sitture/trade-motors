from django.db import models

class Category(models.Model):
    category_parent = models.ForeignKey('self', blank=True, null=True, related_name='category_children')
    category_name = models.CharField('Name', max_length=50, blank=False, null=False)
    category_image = models.ImageField('Image', upload_to='category_images', blank=True)
    category_display_order = models.IntegerField('Display Order', default=999)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        display_text = str(self.category_name)
        if self.category_parent:
            display_text = '{1} ({0})'.format(self.category_parent, self.category_name)
        return display_text
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ('category_display_order', 'category_name',)
    

class VehicleMake(models.Model):
    v_make = models.CharField('Make', max_length=50, blank=False, null=False)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return str(self.v_make)


class Vehicle(models.Model):
    v_category = models.ForeignKey(Category)
    v_make = models.ForeignKey(VehicleMake)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return str(self)


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    v_image = models.ImageField('Image', upload_to='vehicle_images')
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return '%s\'s Image' % self.vehicle