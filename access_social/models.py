from django.db import models
from django.conf import settings

class Token(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
