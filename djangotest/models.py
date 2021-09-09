from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    value = models.IntegerField()


