# Generated by Django 2.1.4 on 2019-06-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190603_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='depart',
            field=models.CharField(choices=[('Academics', 'Academics'), ('Hostel', 'Accomodation')], default='Academics', max_length=6),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='status',
            field=models.CharField(choices=[('Solved', 'Solved'), ('Not Solved', 'Not Solved')], default='Not Solved', max_length=6),
        ),
    ]