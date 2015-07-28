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


class ContactDetailQuerySet(models.QuerySet):
    
    def get_latest_contact_details(self):
        contact_details = self.all().order_by('-timestamp')
        return contact_details[0] if contact_details else None


class ContactDetail(models.Model):
    
    full_name = models.CharField(blank=True, null=True, max_length=100)
    address = models.CharField(blank=False, null=False, max_length=300)
    city = models.CharField(blank=False, null=False, max_length=100)
    postcode = models.CharField(blank=False, null=False, max_length=20)
    county = models.CharField(blank=True, null=True, max_length=50)
    country = models.CharField(blank=True, null=True, max_length=50)
    phone = models.CharField(blank=False, null=False, max_length=50)
    email = models.EmailField(blank=False, null=False)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    objects = ContactDetailQuerySet.as_manager()

    def __str__(self):
        display_text = self.email
        if self.full_name is not None:
            display_text = '{0} ({1})'.format(self.full_name, self.email)
        return display_text
    
    class Meta:
        ordering = ['-timestamp']
