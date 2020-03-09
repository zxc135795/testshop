from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ToImg(models.Model):
    """
    轮播图
    """
    img = models.ImageField(upload_to='toimg', verbose_name='轮播图')

    def __str__(self):
        return self.img


class Category(models.Model):
    """
    导航分类
    """
    name = models.CharField(max_length=20, verbose_name='分类名称')

    def __str__(self):
        return self.name


class CategoryShow(models.Model):
    """
    中间分类
    """
    img = models.ImageField(upload_to='catimg', verbose_name='分类图片')
    name = models.CharField(max_length=20, verbose_name='分类名称')

    def __str__(self):
        return self.name


class Good(models.Model):
    """
    商品
    """
    goodimg = models.ImageField(upload_to='goodimg', verbose_name='商品图')
    name = models.CharField(max_length=20, verbose_name='商品名')
    price = models.FloatField(default=0, verbose_name='价格')
    quan = models.FloatField(default=10, verbose_name='优惠券')
    coupon_price = models.FloatField(default=0, verbose_name='实际价格')
    docs = models.CharField(max_length=20, verbose_name='商品描述')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='所属分类', related_name='goods')

    def __str__(self):
        return self.name


class Youther(models.Model):
    """
    卖家信息（简略）
    """
    img = models.ImageField(upload_to='youimg', verbose_name='卖家头像')
    name = models.CharField(max_length=20, verbose_name='名称')

    def __str__(self):
        return self.name


class ShoeTime(models.Model):
    """
    卖家展示（秀场）
    """
    showimg = models.ImageField(upload_to='showimg', verbose_name='卖家展示图')
    showdocs = models.CharField(max_length=500, verbose_name='卖家推荐言论')
    docs = models.ForeignKey(Youther, on_delete=models.CASCADE, related_name='youer', verbose_name='言论推荐人')

    def __str__(self):
        return self.docs.verbose_name


class User(AbstractUser):
    """
    用户
    """
    telephone = models.CharField(max_length=11, verbose_name='手机号')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    good = models.ManyToManyField(Good, verbose_name='商品')

    def __str__(self):
        return self.user.name
