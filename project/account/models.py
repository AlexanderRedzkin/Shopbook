from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Accounts(models.Model):
    account_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
