# Generated by Django 3.0.3 on 2020-06-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='educ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=55)),
                ('school_location', models.CharField(max_length=55)),
                ('Degree', models.CharField(max_length=55)),
                ('CGPA', models.CharField(max_length=55)),
                ('Field_of_Study', models.CharField(max_length=55)),
                ('Expected_year_of_grad', models.CharField(max_length=55)),
            ],
        ),
    ]