# Generated by Django 4.2.1 on 2023-06-14 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_guest', models.PositiveIntegerField(default=0, verbose_name='Number of guest')),
                ('checkin_date', models.DateField(blank=True, null=True, verbose_name='Checkin date')),
                ('checkout_date', models.DateField(blank=True, null=True, verbose_name='Checkout date')),
                ('is_checkout', models.BooleanField(default=True, verbose_name='Is_Checkout')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0, verbose_name='Status')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='hotel.room', verbose_name='Room')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype')),
            ],
        ),
    ]
