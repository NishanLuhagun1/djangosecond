from django.db import models

class Book(models.Model):
    bk_name = models.CharField(max_length=100)
    bk_number = models.IntegerField()

# Create your models here.
