from django.shortcuts import render

from django.views import View
from rest_framework.views import APIView

from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import *
from rest_framework.decorators import api_view, action
from rest_framework import status, generics, mixins
from django.shortcuts import get_object_or_404
from rest_framework import permissions

from rest_framework import filters


# from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class ShoeTimeViewSets(viewsets.ModelViewSet):
    queryset = ShoeTime.objects.all()
    serializer_class = ShoeTimeSerializer


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class ToImgViewSets(viewsets.ModelViewSet):
    queryset = ToImg.objects.all()
    serializer_class = ToImgSerializer


class CategoryShowViewSets(viewsets.ModelViewSet):
    queryset = CategoryShow.objects.all()
    serializer_class = CategoryShowSerializer


class YoutherviewSets(viewsets.ModelViewSet):
    queryset = Youther.objects.all()
    serializer_class = YoutherSerializer


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# def carts()