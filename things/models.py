from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=520, blank=False)
    quantity = models.IntegerField()


