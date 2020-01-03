from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    is_mvp = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

