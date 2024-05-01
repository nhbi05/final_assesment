# Generated by Django 5.0.4 on 2024-04-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_daycare', '0004_rename_s_parents_name_sitter_s_recommenders_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitter',
            old_name='s_name',
            new_name='s_NIN',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='c_payment',
        ),
        migrations.RemoveField(
            model_name='sitter',
            name='s_timein',
        ),
        migrations.RemoveField(
            model_name='sitter',
            name='s_timeout',
        ),
        migrations.AddField(
            model_name='sitter',
            name='s_contact',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitter',
            name='s_educationlevel',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitter',
            name='s_firstname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitter',
            name='s_lastname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
