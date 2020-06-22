# Generated by Django 3.0.3 on 2020-06-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55)),
                ('position', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
    ]