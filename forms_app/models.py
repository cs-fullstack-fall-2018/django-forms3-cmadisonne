from django.db import models
from datetime import datetime


class FormModel2(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    budget = models.IntegerField()
    numOfEmployees = models.IntegerField()
    establishedDate = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name