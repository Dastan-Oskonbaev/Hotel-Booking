# Generated by Django 4.2.1 on 2023-06-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=30, unique=True, verbose_name='Phone Number')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]