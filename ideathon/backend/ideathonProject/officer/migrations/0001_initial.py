# Generated by Django 3.1 on 2020-09-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Officer_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officerName', models.CharField(max_length=56)),
                ('policeId', models.CharField(max_length=40)),
                ('rank', models.IntegerField()),
                ('retiredDate', models.DateField()),
                ('dateOfHier', models.DateField()),
                ('policeStation', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('district', models.CharField(max_length=40)),
                ('dateOfBirth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('emailId', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64)),
                ('confirmPassword', models.CharField(max_length=64)),
            ],
        ),
    ]