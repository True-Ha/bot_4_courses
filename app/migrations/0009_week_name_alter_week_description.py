# Generated by Django 4.2.1 on 2023-05-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]