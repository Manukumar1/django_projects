from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)

class NextDay(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=100)
    simple_cluster = models.CharField(max_length=100)
    detailed_cluster = models.CharField(max_length=100)
    open_value = models.FloatField(max_length=20)
    high_value = models.FloatField(max_length=20)
    low_value = models.FloatField(max_length=20)
    close_value = models.FloatField(max_length=20)
    oc_d_value = models.FloatField(max_length=20)
    oh_d_value = models.FloatField(max_length=20)
    ol_d_value =models.FloatField(max_length=20)
    co_d1_value = models.FloatField(max_length=20)
