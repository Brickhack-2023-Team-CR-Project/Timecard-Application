from django.db import models

# Create your models here.
class Clock_Data(models.Model):
    name = models.CharField(max_length=200)
    clock_in_time = models.CharField(max_length=200)
    clock_out_time = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.name