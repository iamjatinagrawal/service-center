# Generated by Django 2.2.5 on 2020-01-09 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCenters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketID', models.PositiveIntegerField(unique=True)),
                ('receivedOn', models.DateField()),
                ('customerName', models.CharField(max_length=100)),
                ('phoneNumber', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
