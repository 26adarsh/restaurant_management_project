from django.db import models

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