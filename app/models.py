from django.contrib.auth.models import AbstractUser
from django.db import models


class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class MyUser(AbstractUser):
    tele_name = models.CharField(max_length=250)
    tele_username = models.CharField(max_length=250)
    tele_user_id = models.CharField(max_length=250)
    email = models.EmailField(null=True, blank=True)
    payment = models.TextField(null=True, blank=True)
    # ip = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tele_name)


class Payment(models.Model):
    user_id = models.CharField(max_length=120, null=True, blank=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.payment_info)


class Training(models.Model):
    name = models.CharField(max_length=300)

    class Day(models.TextChoices):
        Monday = "Mon"
        Wednesday = "Wed"
        Friday = "Fri"

    class Week(models.TextChoices):
        First_week = "1st_week"
        Second_week = "2nd_week"
        Third_week = "3rd_week"
        Fourth_week = "4th_week"

    train_week = models.CharField(max_length=300, choices=Week.choices)
    train_day = models.CharField(max_length=300, choices=Day.choices)

#
# class Days(models.Model):
#     day = models.CharField(max_length=100, null=True, blank=True)
#
#     def __str__(self):
#         return str(self.day)
#
#     class Meta:
#         verbose_name = 'Day'
#         verbose_name_plural = 'Days'
#
#
# class Week(models.Model):
#
#     CHOICES = (
#         ('MON', 'Monday'),
#         ('WED', 'Wednesday'),
#         ('FRI', 'Friday'),
#     )
#     #  choices=Days.day
#
#     days = models.CharField(max_length=300, choices=CHOICES, null=True)
#     name = models.CharField(max_length=100, null=True, blank=True)
#
#     def __str__(self):
#         return str(self.name)


