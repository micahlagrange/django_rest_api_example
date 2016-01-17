from django.db import models


# Create your models here.
class RestUser(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    mail = models.EmailField(null=True, blank=True)
    blurb = models.TextField(null=True, blank=True)
