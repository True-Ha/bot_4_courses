from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    tele_name = models.CharField(max_length=250)
    tele_username = models.CharField(max_length=250)
    tele_user_id = models.CharField(max_length=250)
    email = models.EmailField(null=True, blank=True)
