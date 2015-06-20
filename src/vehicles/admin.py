from django.contrib import admin
from .models import *
# Register your models here.

# register the vehicle categories model
class VehicleCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


# register the category type model
class VehicleCategoryTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = CategoryType


# register the vehicle model
class VehicleAdmin(admin.ModelAdmin):
    class Meta:
        model = Vehicle


admin.site.register(Category, VehicleCategoryAdmin)
admin.site.register(CategoryType, VehicleCategoryTypeAdmin)
admin.site.register(Vehicle, VehicleAdmin)