# Generated by Django 4.2.4 on 2023-09-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_alter_openingtime_clinic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, upload_to='images/services')),
                ('doctor', models.ManyToManyField(related_name='services', to='clinic.doctor')),
            ],
        ),
    ]
