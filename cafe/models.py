from django.db import models

# Create your models here.
class Category(models.Model):
    name  = models.CharField(max_length=50, unique=True)
    is_special = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/',blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class AboutUs(models.Model):
    header = models.CharField(max_length=100, default="About Breeze Cafe")
    description = models.TextField()
    history_title = models.CharField(max_length=100, default="How We Began")
    history_description = models.TextField()
    image1 = models.ImageField(upload_to='about_images/',blank=True, null=True)
    image2 = models.ImageField(upload_to='about_images/',blank=True, null=True)
    
    def __str__(self):
        return self.header
    