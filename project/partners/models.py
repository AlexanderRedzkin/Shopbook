from django.db import models

# Create your models here.
class Partners(models.Model):
    company = models.CharField(max_length=50)
