

# Create your models here.
from django import models

class MenuCategory(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
        