from django.contrib import admin

from .models import MyUser, Payment, Training


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_week', 'train1', 'train2',
                    'train3', 'train4', 'train5', 'train6', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    save_as = True


admin.site.register(MyUser)
admin.site.register(Payment)
admin.site.register(Training, TrainingAdmin)
