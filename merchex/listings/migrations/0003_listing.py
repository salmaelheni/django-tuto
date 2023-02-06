# Generated by Django 3.1.7 on 2023-02-06 15:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20230206_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('sold', models.BooleanField(default=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band')),
            ],
        ),
    ]
