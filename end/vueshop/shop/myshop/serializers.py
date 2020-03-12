# ProjectName:Lvueshop
# FileName:serializers
# author:asus
# datetime:2020/3/9 13:00
# software: PyCharm
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"


class CategoryShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryShow
        fields = "__all__"


class YoutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youther
        fields = "__all__"


class ToImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToImg
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ShoeTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoeTime
        fields = "__all__"
