# Generated by Django 5.0.4 on 2024-04-30 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_daycare', '0007_remove_baby_c_stay_remove_payment_paye_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorystay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('s_lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('s_age', models.IntegerField(blank=True, null=True)),
                ('s_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('s_location', models.CharField(blank=True, default='Kabalagala', max_length=100, null=True)),
                ('s_nextofkin', models.CharField(blank=True, max_length=100, null=True)),
                ('s_recommenders_name', models.CharField(blank=True, max_length=200, null=True)),
                ('s_NIN', models.CharField(blank=True, max_length=200, null=True)),
                ('s_educationlevel', models.CharField(blank=True, max_length=200, null=True)),
                ('s_contact', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('b_lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('parents_name', models.CharField(blank=True, max_length=200, null=True)),
                ('timeIn', models.DateTimeField(blank=True, null=True)),
                ('timeOut', models.DateTimeField(blank=True, null=True)),
                ('c_stay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_daycare.categorystay')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('pay_no', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, default='Ugx', max_length=10, null=True)),
                ('paye', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_daycare.baby')),
            ],
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, default='Ugx', max_length=10, null=True)),
                ('paye', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_daycare.baby')),
            ],
        ),
    ]
