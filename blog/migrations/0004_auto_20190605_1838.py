# Generated by Django 2.1.4 on 2019-06-05 13:08

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190605_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='grievance_id',
            field=models.CharField(default=blog.models.grievance_number, max_length=20),
        ),
    ]