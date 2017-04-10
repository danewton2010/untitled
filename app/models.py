from django.db import models

# Create your models here.
class CCBZ(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=30)
    train = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    work_time = models.FloatField()
    work_bonus = models.FloatField()
    in_time = models.DateTimeField()
    out_time = models.DateTimeField()
    rest_time = models.FloatField()
    rest_bonus = models.FloatField()
    sum_bonus = models.FloatField()
