# Generated by Django 3.2 on 2021-06-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0009_alter_bbs_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
