# Generated by Django 3.2 on 2021-06-07 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0016_alter_bbs_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='week',
        ),
    ]