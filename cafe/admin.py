from django.contrib import admin
from django.contrib import admin
from .models import Category, FoodItem, AboutUs

# Register your models here.
admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(AboutUs)
