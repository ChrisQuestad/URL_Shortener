from django.db import models

class URL(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=8, primary_key=True)
