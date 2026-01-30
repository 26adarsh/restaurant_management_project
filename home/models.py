from django.db import models
from .models import MenuItem
import datetime
# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique = True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class DailySpecial(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_random_special():
        specials=DailySpecial.objects.filter(is_available=True)
        if not specials.exists():
            return None
        return specials.order_by('?').first()

    
class NutritionalInformation(models.Model):
    menu_item = models.ForeignKey(
        MenuItem,
        on-delete=models.CASCADE,
        related_name='nutritional_info'
    )
    calories = models.IntegerField()
    protein_grams=models.DecimalField(max_digits=5,decimal_places=2)
    fat_grams=models.DecimalField(max_digits=5,decimal_places=2)
    carbohydrate_grams=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name}-{self.calories}kcal"

class Ingredient(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category=models.ForeignKey(MenuCategory,on_delete=models.CASCADE,related_name='items')
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class DailySpecialManager(models.Manager):
    def upcoming(self):
        today=datetime.date.today()
        return self.filter(date__gte=today)

class DailySpecial(models.Model):
    name=models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date=models.DateField()

    objects=DailySpecialManager()
    def __str__(self):
        return self.title

class OrderItem(models.Model):
    order = models.ForeignKey('Order',on_delete=models.CASCADE)
    menu_item=models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name='orderitem'
    )
    quantity = models.PositiveIntegerField(default=1)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    address=models.TextField()
    city=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    operating_days=models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Comma-seprated days e.g. Mon,Tue,Wed,Thu,Fri"
    )
    def __str__(self):
        return self.name