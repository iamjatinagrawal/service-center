# Generated by Django 2.2.5 on 2020-01-09 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support_ticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='customerName',
        ),
    ]
