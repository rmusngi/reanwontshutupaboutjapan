# Generated by Django 2.2.2 on 2019-06-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('forex', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('weather', models.DecimalField(decimal_places=2, max_digits=3)),
                ('main_image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('event_name_1', models.CharField(blank=True, max_length=200)),
                ('event_desc_1', models.CharField(blank=True, max_length=1000)),
                ('event_photo_1', models.ImageField(blank=True, upload_to='photos/events/%Y/%m/%d')),
                ('event_name_2', models.CharField(blank=True, max_length=200)),
                ('event_desc_2', models.CharField(blank=True, max_length=1000)),
                ('event_photo_2', models.ImageField(blank=True, upload_to='photos/events/%Y/%m/%d')),
                ('event_name_3', models.CharField(blank=True, max_length=200)),
                ('event_desc_3', models.CharField(blank=True, max_length=1000)),
                ('event_photo_3', models.ImageField(blank=True, upload_to='photos/events/%Y/%m/%d')),
                ('discount1_name', models.CharField(blank=True, max_length=50)),
                ('discount1_url', models.URLField(blank=True)),
                ('discount2_name', models.CharField(blank=True, max_length=50)),
                ('discount2_url', models.URLField(blank=True)),
                ('discount3_name', models.CharField(blank=True, max_length=50)),
                ('discount3_url', models.URLField(blank=True)),
                ('attraction_name1', models.CharField(blank=True, max_length=50)),
                ('attraction_url1', models.URLField(blank=True)),
                ('attraction_image1', models.ImageField(blank=True, upload_to='photos/attraction/%Y/%m/%d')),
                ('attraction_name2', models.CharField(blank=True, max_length=50)),
                ('attraction_url2', models.URLField(blank=True)),
                ('attraction_image2', models.ImageField(blank=True, upload_to='photos/attraction/%Y/%m/%d')),
                ('attraction_name3', models.CharField(blank=True, max_length=50)),
                ('attraction_url3', models.URLField(blank=True)),
                ('attraction_image3', models.ImageField(blank=True, upload_to='photos/attraction/%Y/%m/%d')),
            ],
        ),
    ]
