# Generated by Django 4.2.1 on 2023-05-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_days_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('train_week', models.CharField(choices=[('1st_week', 'First Week'), ('2nd_week', 'Second Week'), ('3rd_week', 'Third Week'), ('4th_week', 'Fourth Week')], max_length=300)),
                ('train_day', models.CharField(choices=[('Mon', 'Monday'), ('Wed', 'Wednesday'), ('Fri', 'Friday')], max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Days',
        ),
        migrations.DeleteModel(
            name='Week',
        ),
    ]
