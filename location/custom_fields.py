from django.db import models

class CustomValues(models.Model)
    def events1(models.Model):
            event_name = models.CharField(max_length=200)
            event_desc = models.CharField(max_length=1000)
            event_photo = models.ImageField(upload_to='/photos/events/%Y/%m/%d')
    def events2(models.Model):
            event_name = models.CharField(max_length=200, blank=True)
            event_desc = models.CharField(max_length=1000, blank=True)
            event_photo = models.ImageField(upload_to='/photos/events/%Y/%m/%d', blank=True)
    def events3(models.Model):
            event_name = models.CharField(max_lengtg=200, blank=True)
            event_desc = models.CharField(max_length=1000, blank=True)
            event_photo = models.ImageField(upload_to='/photos/events/%Y/%m/%d', blank=True)
    def events4(models.Model):
            event_name = models.CharField(max_length=200, blank=True)
            event_desc = models.CharField(max_length=1000, blank=True)
            event_photo = models.ImageField(upload_to='/photos/events/%Y/%m/%d', blank=True)
    def events5(models.Model):
            event_name = models.CharField(max_length=200, blank=True)
            event_desc = models.CharField(max_length=1000, blank=True)
            event_photo = models.ImageField(upload_to='/photos/events/%Y/%m/%d', blank=True)
    def discount1(models.Model):
            discount1_name = models.CharField(max_length=50, blank=True)
            discount1_url = models.URLField(blank=True)
    def discount2(models.Model):
            discount1_name = models.CharField(max_length=50, blank=True)
            discount1_url = models.URLField(blank=True)
    def discount3(models.Model):
            discount1_name = models.CharField(max_length=50, blank=True)
            discount1_url = models.URLField(blank=True)
    def attractions1(models.Model):
           attraction_name = models.CharField(max_length=50, blank=True)
           attraction_url = models.URLField(blank=True)
    def attractions2(models.Model):
           attraction_name = models.CharField(max_length=50, blank=True)
           attraction_url = models.URLField(blank=True)
    def attractions3(models.Model):
           attraction_name = models.CharField(max_length=50, blank=True)
           attraction_url = models.URLField(blank=True)