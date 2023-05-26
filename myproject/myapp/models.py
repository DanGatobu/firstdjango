from django.db import models

# Create your models here.
class product(models.Model):
    namee=models.CharField(max_length=300 ,default='name')
    price=models.FloatField()
    quantity=models.IntegerField()
    