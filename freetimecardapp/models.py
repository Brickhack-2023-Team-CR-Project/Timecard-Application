from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=200)
    clock_in_data = models.JSONField(null=True)

    def __str__(self):
        return self.name