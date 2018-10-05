from django.db import models
from django.conf import settings

# Create your models here.


class TM(models.Model):
    talker = models.CharField(max_length=40, blank=False)
    message = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.talker + " " + self.message


