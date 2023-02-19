from django.db import models


class Shortner(models.Model):
    url = models.CharField(max_length=2000)
    shorturl = models.CharField(max_length=50)
