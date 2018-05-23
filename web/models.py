# -*- coding: UTF-8 -*-
from django.db import models

# 日誌
class Diary(models.Model):
    memo = models.TextField(verbose_name='內容')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.memo
      
# 帳目
class Money(models.Model):
    CHOICES = (
      (1, "飲食"),
      (2, "衣服"),
      (3, "交通"),
      (4, "教育"),
      (5, "娛樂"),
      (6, "其它"),
    )    
    item = models.CharField(max_length=30, verbose_name='項目')
    kind = models.IntegerField(default=0, choices=CHOICES, verbose_name='類別')
    price = models.IntegerField(default=0, verbose_name='金額')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item