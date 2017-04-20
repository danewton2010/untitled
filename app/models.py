from django.db import models

# Create your models here.
class CCBZ(models.Model):
    code = models.IntegerField(verbose_name="编码")
    name = models.CharField(max_length=30,verbose_name="姓名")
    train = models.CharField(max_length=30,verbose_name="车次")
    start_time = models.DateTimeField(verbose_name="出乘开始")
    stop_time = models.DateTimeField(verbose_name="出乘结束")
    work_time = models.FloatField(verbose_name="出乘时间")
    work_bonus = models.FloatField(verbose_name="出乘补助")
    in_time = models.DateTimeField(verbose_name="休息开始")
    out_time = models.DateTimeField(verbose_name="休息结束")
    rest_time = models.FloatField(verbose_name="休息时间")
    rest_bonus = models.FloatField(verbose_name="休息补助")
    sum_bonus = models.FloatField(verbose_name="合计补助")


