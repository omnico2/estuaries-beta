# Generated by Django 3.1.4 on 2020-12-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201220_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profilepic',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
