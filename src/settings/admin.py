from django.contrib import admin
from settings.models import ContactDetail

# register the contact details model
class ContactDetailAdmin(admin.ModelAdmin):
    
    class Meta:
        model = ContactDetail


# Register your models here.
admin.site.register(ContactDetail, ContactDetailAdmin)