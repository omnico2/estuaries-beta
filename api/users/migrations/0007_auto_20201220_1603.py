# Generated by Django 3.1.4 on 2020-12-20 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_profilepic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='joined_at',
            new_name='member_since',
        ),
    ]
