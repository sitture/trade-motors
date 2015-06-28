from django.contrib import admin
from .models import *
# Register your models here.

# register the vehicle categories model
class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'category_display_order']
    
    class Meta:
        model = Category


# register the vehicle model
class VehicleAdmin(admin.ModelAdmin):
    class Meta:
        model = Vehicle


class VehicleMakeAdmin(admin.ModelAdmin):
    class Meta:
        model = VehicleMake


admin.site.register(Category, VehicleCategoryAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleMake, VehicleMakeAdmin)