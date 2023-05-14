from django.contrib import admin

from .models import MyUser, Payment, Training

admin.site.register(MyUser)
admin.site.register(Payment)
admin.site.register(Training)
# admin.site.register(Week)