# Generated by Django 2.0.6 on 2018-09-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Company name', max_length=100, verbose_name='Company name')),
                ('address', models.CharField(max_length=100, verbose_name='Company address')),
                ('phone', models.CharField(max_length=20, verbose_name='Company phone number')),
                ('contact_person', models.CharField(max_length=20, verbose_name='Contact person')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('inactive', models.BooleanField(default=False, verbose_name='Inactive')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
