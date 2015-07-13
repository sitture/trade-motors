from django.contrib import admin
from settings.models import ContactDetail, Social

# register the contact details model
class ContactDetailAdmin(admin.ModelAdmin):
    
    class Meta:
        model = ContactDetail


class SocialAdmin(admin.ModelAdmin):
    list_display = ['service', 'url']
    
    class Meta:
        model = Social


# Register your models here.
admin.site.register(ContactDetail, ContactDetailAdmin)
admin.site.register(Social, SocialAdmin)