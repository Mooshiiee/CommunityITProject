# Generated by Django 4.2.9 on 2024-02-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_classes_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='descritption',
        ),
        migrations.AddField(
            model_name='classes',
            name='description',
            field=models.CharField(default='default description bruv', max_length=512),
            preserve_default=False,
        ),
    ]