from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class SliderImage(models.Model):
    banner = ProcessedImageField(
        blank=False, null=False,
        upload_to='slider',
        processors=[ResizeToFill(1170, 375)],
        format='JPEG',
        options={'quality': 100}
    )  # cannot be null
    caption = RichTextField('Caption (Optional)', blank=True, null=True)

    def __str__(self):
        return str(self.banner)


class Social(models.Model):

    SERVICE_CHOICES = (
        ('facebook', 'Facebook'),
        ('google-plus', 'Google+'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram')
    )

    service = models.CharField('Service', max_length=50, blank=False,
                               choices=SERVICE_CHOICES)
    url = models.URLField('Page Link', null=False, blank=False)

    def __str__(self):
        return str(self.service)


class ContactDetail(models.Model):
    full_name = models.CharField(
        'FullName (Optional)', max_length=150, blank=True, null=True)
    address = models.CharField('Address', blank=True, max_length=500)
    postcode = models.CharField('Postcode', blank=True, max_length=150)
    city = models.CharField('City', blank=True, max_length=150)
    country = models.CharField('Country', blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=150)
    email = models.CharField('Email', blank=False, null=False, max_length=300)

    def __str__(self):
        display_text = self.email
        if self.full_name is not None:
            display_text = '{0} ({1})'.format(self.full_name, self.email)
        return display_text
