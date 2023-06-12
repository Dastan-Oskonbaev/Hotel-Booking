# Generated by Django 4.2.1 on 2023-06-09 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_guest', models.PositiveIntegerField(default=0)),
                ('checkin_date', models.DateField(auto_now_add=True)),
                ('checkout_date', models.DateField(auto_now_add=True)),
                ('is_checkout', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype')),
            ],
        ),
    ]