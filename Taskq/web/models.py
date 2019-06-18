from django.db import models


class DataBase(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=1000)
    status = models.IntegerField(default=0)
