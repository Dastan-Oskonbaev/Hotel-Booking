# Generated by Django 4.2.1 on 2023-06-12 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateField(blank=True, null=True, verbose_name='Checkin date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateField(blank=True, null=True, verbose_name='Checkout date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='is_checkout',
            field=models.BooleanField(default=True, verbose_name='Is_Checkout'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='num_of_guest',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of guest'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='hotel.room', verbose_name='Room'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0, verbose_name='Status'),
        ),
    ]