from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize


class CategoryQuerySet(models.QuerySet):

    def get_main_categories(self):
        return self.filter(category_parent=None)

    def get_sub_categories(self):
        return self.exclude(category_parent=None)

    def get_sub_categories_by_category(self, category):
        return self.filter(category_parent=category)

    def get_categories_with_sub_categories(self):
        tree = []
        for category in self.get_main_categories():
            # get sub_categories
            sub_categories = self.get_sub_categories_by_category(category)
            # add category and sub_categories into a tmp list
            tmp = [category, list(sub_categories)]
            # add the tmp list to main categories tree list
            tree.append(tmp)
        return tree

    def get_category_by_slug(self, slug):
        category = None
        try:
            category = self.get(slug=slug)
        except Category.DoesNotExist:
            return category

        return category

    def get_home_page_categories(self):
        return self.filter(show_on_home_page=True)


class Category(models.Model):
    category_parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='category_children', on_delete=models.DO_NOTHING)
    category_name = models.CharField(
        'Name', max_length=50, blank=False, null=False)
    category_image = models.ImageField(
        'Image', upload_to='categories', blank=True)
    category_display_order = models.IntegerField('Display Order', default=999)
    show_on_home_page = models.BooleanField('Show on Homepage?', default=False)
    slug = models.SlugField(unique=True)

    thumbnail = ImageSpecField(
        source='category_image',
        processors=[SmartResize(270, 160)],
        format='JPEG',
        options={'quality': 80}
    )

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


class VehicleMakeQuerySet(models.QuerySet):

    def get_make_by_slug(self, slug):
        make = None
        try:
            make = self.get(slug=slug)
        except VehicleMake.DoesNotExist:
            return make

        return make


class VehicleMake(models.Model):
    v_make = models.CharField('Make', max_length=50, blank=False, null=False)
    slug = models.SlugField(unique=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = VehicleMakeQuerySet.as_manager()

    def __unicode__(self):
        return str(self.v_make)

    class Meta:
        verbose_name_plural = 'Makes'
        verbose_name = 'Make'


class VehicleQuerySet(models.QuerySet):

    @classmethod
    def process_category(self, category):
        categories = []
        # check if a given category is a parent category
        if category and category.category_parent is None:
            # get sub_categories
            categories = list(
                Category.objects.get_sub_categories_by_category(category))
        categories.append(category)
        return categories

    def get_vehicles_by_category(self, category):
        # process category into a list
        categories = self.process_category(category)
        return self.filter(category__in=categories).order_by('-timestamp')

    def get_vehicles_by_make(self, make):
        return self.filter(make=make).order_by('-timestamp')

    def get_vehicles_by_category_and_make(self, category, make):
        categories = self.process_category(category)
        return self.filter(
            category__in=categories,
            make=make
        ).order_by('-timestamp')


class Vehicle(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    make = models.ForeignKey(VehicleMake, on_delete=models.DO_NOTHING)
    model = models.CharField('Model', max_length=100)
    year = models.IntegerField("Year (E.g. 1990)",
                               blank=True, null=True)
    price = models.IntegerField('Price (Optional)',
                                blank=True, null=True)
    FUEL_CHOICES = (
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel')
    )
    fuel_type = models.CharField(
        'Fuel Type', max_length=50,
        null=True, blank=True,
        choices=FUEL_CHOICES)
    TRANSMISSION_CHOICES = (
        ('automatic', 'Automatic'),
        ('manual', 'Manual')
    )
    transmission = models.CharField(
        'Transmission', max_length=50,
        null=True, blank=True,
        choices=TRANSMISSION_CHOICES)
    colour = models.CharField('Colour', max_length=50,
                              blank=True, null=True)
    mileage = models.IntegerField(
        'Mileage', null=True, blank=True)
    desc = RichTextField("Description")
    slug = models.SlugField()

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = VehicleQuerySet.as_manager()

    def __unicode__(self):
        if not self.year:
            return '{0} {1}'.format(
                self.make, self.model)
        display_text = '{0} {1} {2}'.format(
            self.make, self.model, self.year)
        return display_text

    class Meta:
        ordering = ['-timestamp']


class VehicleImageQuerySet(models.QuerySet):

    def get_main_image(self):
        # get all the images with flag main_image
        main_image_list = self.filter(main_image=True).order_by('-timestamp')
        # return only the latest main_image
        return main_image_list[0] if main_image_list else None

    def get_additional_images(self):
        return self.exclude(main_image=True).order_by('-timestamp')


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.DO_NOTHING)
    image = models.ImageField('Image', upload_to='vehicles')
    main_image = models.BooleanField('Main Image?', default=False)

    thumbnail = ImageSpecField(
        source='image',
        processors=[SmartResize(270, 160)],
        format='JPEG',
        options={'quality': 70}
    )

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = VehicleImageQuerySet.as_manager()

    def __unicode__(self):
        return "{0}'s Image".format(self.vehicle)

    class Meta:
        verbose_name_plural = 'Images'
        verbose_name = 'Image'
        ordering = ['vehicle', '-timestamp']
