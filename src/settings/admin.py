from django.contrib import admin
from settings.models import ContactDetail, Social, SliderImage


class ContactDetailAdmin(admin.ModelAdmin):

    class Meta:
        model = ContactDetail


class SocialAdmin(admin.ModelAdmin):
    list_display = ['service', 'url']

    class Meta:
        model = Social


class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['banner', 'caption']

    class Meta:
        model = SliderImage

# Register your models here.
admin.site.register(ContactDetail, ContactDetailAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
