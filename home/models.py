

# Create your models here.
from django import models

class MenuCategory(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
        
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    @staticmethod
    def get_random_special():
        """
        Returns one random DailySpecial from the database.
        If no specials exist, returns None.
        """

        specials = DailySpecial.objects.all()
        if not sprcials.exists():
            return None
        return specials.order_by('?').first()
        