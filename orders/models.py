

# Create your models here.
from django.db import models
from django.utils import timezone

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = moedels.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code

    def is_valid(self):
        today = timezone.now().date()
        return (
            self.is_active and
            self.valid_from <=today <= self.valid_until

        ) 

from django.db import models

class orderStatus(models.Model)
    name = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name
