from django.db import models

#Importing datetime
from datetime import datetime
from datetime import date

# Create your models here.
class Clock_Data(models.Model):

    now_date = date.today()
    current_date = now_date.strftime("%m/%d/%y")

    name = models.CharField(max_length=30)
    clock_in_time = models.CharField(max_length=20)
    clock_in_date = models.CharField(max_length=20, default=current_date)
    clock_out_time = models.CharField(max_length=20,null=True)
    clock_out_date = models.CharField(max_length=20, null=True, default=current_date)

    def __str__(self):
        return self.name