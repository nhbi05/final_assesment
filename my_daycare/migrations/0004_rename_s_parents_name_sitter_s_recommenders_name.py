# Generated by Django 5.0.4 on 2024-04-28 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_daycare', '0003_rename_b_name_baby_b_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitter',
            old_name='s_parents_name',
            new_name='s_recommenders_name',
        ),
    ]
