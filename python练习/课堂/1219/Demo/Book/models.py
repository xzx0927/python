from datetime import datetime

from django.db import models


class BookLei(models.Model):
    name = models.CharField(max_length=40, null=True, verbose_name='名称')
    miaoshu = models.TextField(verbose_name='描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = '类型'


class Book(models.Model):
    name = models.CharField(max_length=40, null=True, verbose_name='名称')
    type = models.ForeignKey(BookLei, null=True, on_delete=models.CASCADE, verbose_name='类型')
    author = models.CharField(max_length=10, null=True, verbose_name='作者')
    publish = models.CharField(max_length=20, null=True, verbose_name='出版社')
    time = models.DateField(default=datetime.now, verbose_name='出版时间')
    cover = models.ImageField(upload_to='upload/covers', default='upload/covers/abc.png', verbose_name='封面')#数据库中cover参数covers是文件名称
    price = models.FloatField(verbose_name='价格')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'
