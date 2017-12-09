from django.db import models

class URL(models.Model):
    url = models.URLField
    shoretened_url = models.CharField(max_length=8, primary_key=True)
