from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


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
    has_payment = models.BooleanField(default=False)

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
    description_week = models.TextField(null=True)
    train1 = models.TextField(null=True)
    train2 = models.TextField(null=True)
    train3 = models.TextField(null=True)
    train4 = models.TextField(null=True)
    train5 = models.TextField(null=True)
    train6 = models.TextField(null=True)
    text_after_train = models.TextField(null=True)


    slug = models.SlugField(max_length=130, unique=True, null=True, db_index=True, verbose_name="URL")


    class Day(models.TextChoices):
        Monday = "Понедельник"
        Wednesday = "Среда"
        Friday = "Пятница"

    class Week(models.TextChoices):
        First_week = "1 неделя"
        Second_week = "2 неделя"
        Third_week = "3 неделя"
        Fourth_week = "4 неделя"

    train_week = models.CharField(max_length=300, choices=Week.choices)
    train_day = models.CharField(max_length=300, choices=Day.choices)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('train_detail', kwargs={"slug": self.slug})















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


