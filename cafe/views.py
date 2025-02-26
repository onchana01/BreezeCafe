from django.shortcuts import render
from .models import Category, FoodItem, AboutUs

# Create your views here.
def index(request):
    
    # Drink Menu categories (non-special)
    drink_categories = Category.objects.filter(is_special=False)
    drink_items = {cat: FoodItem.objects.filter(category=cat) for cat in drink_categories}
    
    #special Meals Category
    special_categories = Category.objects.filter(is_special=True)
    special_items = FoodItem.objects.filter(category__in=special_categories)
    
    #About Us Content 
    about_us = AboutUs.objects.first()
    
    context = {
        'drink_items': drink_items,
        'special_items': special_items,
        'about_us': about_us,
    }
    return render(request, 'cafe/index.html', context)