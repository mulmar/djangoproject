# Generated by Django 2.1.4 on 2019-01-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.EmailField(max_length=15)),
                ('address', models.EmailField(max_length=200)),
                ('zipcode', models.EmailField(max_length=8)),
                ('city', models.EmailField(max_length=50)),
            ],
        ),
    ]
