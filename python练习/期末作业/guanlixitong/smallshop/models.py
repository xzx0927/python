from django.db import models


class place(models.Model):
    place_name = models.CharField(max_length=40, null=True, verbose_name="地点")
    detail_place = models.TextField(verbose_name="详细地点描述")

    def __str__(self):  # 设置外键（当有人使用外键时调用place_name）
        return self.place_name

    class Meta:
        verbose_name = "地点"
        verbose_name_plural = "地点"


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=40, null=True, verbose_name='名字')
    password = models.CharField(max_length=40, null=True, verbose_name='密码')
    place = models.ForeignKey(place, null=True, on_delete=models.CASCADE, verbose_name='地点')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"


class shop(models.Model):
    name = models.CharField(max_length=40, null=True, verbose_name='商品名称')
    msg=models.ImageField(upload_to='upload/covers', default='upload/covers/abc.png', verbose_name='商品图片')
    place = models.ForeignKey(place, null=True, on_delete=models.CASCADE, verbose_name='商品地点')
    prime_cost = models.FloatField(null=True, verbose_name='进货价格')
    price = models.FloatField(null=True, verbose_name='价格')  # 出售结果
    quantity = models.IntegerField(null=True, verbose_name='数量')
    residual_quantity = models.IntegerField(null=True, verbose_name='剩余数量')  # 剩余数量

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"
