from django.contrib import admin
from vehicles.models import Category, Vehicle, VehicleMake, VehicleImage
# Register your models here.


class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'category_display_order']
    prepopulated_fields = {'slug': ('category_name',)}

    class Meta:
        model = Category


# register the vehicle model
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'category']
    list_filter = ('category', 'make', 'year')
    prepopulated_fields = {'slug': ('make', 'model', 'transmission', 'year')}

    class Meta:
        model = Vehicle


class VehicleMakeAdmin(admin.ModelAdmin):

    class Meta:
        model = VehicleMake


class VehicleImageAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'image', 'main_image']
    list_filter = ['vehicle']

    class Meta:
        model = VehicleImage


admin.site.register(Category, VehicleCategoryAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleMake, VehicleMakeAdmin)
admin.site.register(VehicleImage, VehicleImageAdmin)
