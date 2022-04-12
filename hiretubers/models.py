from django.db import models
from datetime import datetime
# Create your models here.

class HireTubers(models.Model):
    tuber_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.TextField()
    user_id = models.IntegerField(blank=True,)
    created_date = models.DateTimeField(blank=True,default = datetime.now)

    def __str__(self):
        return self.email