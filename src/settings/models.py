from django.db import models

# Create your models here.
class SliderImage(models.Model):
    pass    
    #banner = models.ImageField(blank=False, null=False, upload_to='slider') # cannot be null
    #caption = models.TextField('Caption (Optional)', blank=True, null=True)


class Social(models.Model):
    
    SERVICE_CHOICES  = (
        ('facebook', 'Facebook'),
        ('google-plus', 'Google+'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram')
    )
    
    service = models.CharField('Service', max_length=50, blank=False,
        choices=SERVICE_CHOICES
    )
    url = models.URLField('Page Link', null=False, blank=False)

    def __str__(self):
        return str(self.service)

class ContactDetail(models.Model):
    
    full_name = models.CharField('FullName (Optional)', max_length=150, blank=True, null=True)
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
