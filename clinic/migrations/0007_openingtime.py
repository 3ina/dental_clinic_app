# Generated by Django 4.2.4 on 2023-09-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_doctor_clinic'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255)),
                ('clinic', models.ManyToManyField(to='clinic.clinic')),
            ],
        ),
    ]
