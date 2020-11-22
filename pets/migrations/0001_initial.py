# Generated by Django 3.1.2 on 2020-11-22 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pet_image')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('birth_date', models.DateField()),
                ('pet_type', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('vaccinated', models.BooleanField(default=False)),
                ('castrated', models.BooleanField(default=False)),
                ('dewormed', models.BooleanField(default=False)),
                ('vulnerable', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
