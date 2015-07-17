from django.db import models
from ckeditor.fields import RichTextField


class CategoryQuerySet(models.QuerySet):
    
    def main_categories(self):
        return self.filter(category_parent=None)
    
    def sub_categories(self):
        return self.exclude(category_parent=None)
    
    def sub_categories_by_category(self, category):
        return self.filter(category_parent=category)
    
    def combined(self):
        tree = []
        for category in self.main_categories():
            # get sub_categories
            sub_categories = self.sub_categories_by_category(category)
            # add category and sub_categories into a tmp list
            tmp = [category, list(sub_categories)]
            # add the tmp list to main categories tree list
            tree.append(tmp)
        return tree


class Category(models.Model):
    category_parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='category_children')
    category_name = models.CharField(
        'Name', max_length=50, blank=False, null=False)
    category_image = models.ImageField(
        'Image', upload_to='categories', blank=True)
    category_display_order = models.IntegerField('Display Order', default=999)
    slug = models.SlugField(unique=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    objects = CategoryQuerySet.as_manager()

    def __unicode__(self):
        display_text = str(self.category_name)
        if self.category_parent:
            display_text = '{1} ({0})'.format(
                self.category_parent, self.category_name)
        return display_text

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['category_display_order', 'category_name']


class VehicleMake(models.Model):
    v_make = models.CharField('Make', max_length=50, blank=False, null=False)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.v_make)

    class Meta:
        verbose_name_plural = 'Makes'
        verbose_name = 'Make'


class Vehicle(models.Model):
    category = models.ForeignKey(Category)
    make = models.ForeignKey(VehicleMake)
    model = models.CharField('Model', max_length=100)
    year = models.IntegerField("Year (E.g. 1990)", blank=True, null=True)
    FUEL_CHOICES = (
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel')
    )
    fuel_type = models.CharField(
        'Fuel Type', max_length=50, null=True, blank=True, choices=FUEL_CHOICES)
    TRANSMISSION_CHOICES = (
        ('automatic', 'Automatic'),
        ('manual', 'Manual')
    )
    transmission = models.CharField(
        'Transmission', max_length=50, null=True, blank=True, choices=TRANSMISSION_CHOICES)
    colour = models.CharField('Colour', max_length=50, blank=True, null=True)
    mileage = models.IntegerField(
        'Mileage', null=True, blank=True)
    desc = RichTextField("Description")
    slug = models.SlugField()

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        display_text = '{0} {1} {2}'.format(self.make, self.model, self.year)
        return display_text

    class Meta:
        ordering = ['-timestamp']


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    image = models.ImageField('Image', upload_to='vehicles')
    main_image = models.BooleanField('Main Image?', default=False)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "{0}'s Image".format(self.vehicle)

    class Meta:
        verbose_name_plural = 'Images'
        verbose_name = 'Image'
        ordering = ['vehicle', '-timestamp']
