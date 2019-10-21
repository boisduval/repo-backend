# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializers
from rest_framework import viewsets, filters, pagination


# Create your views here.

class PageSet(pagination.PageNumberPagination):
    # 每页显示多少个
    page_size = 7
    # 默认每页显示7个
    page_size_query_param = "size"
    # 最大页数
    max_page_size = 10
    # 获取页码数的
    page_query_param = "page"


class StudentViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = TodoItem.objects.all().order_by('-id')
    # 指定序列化的类
    serializer_class = TodoItemSerializers
    # 指定分页配置
    pagination_class = PageSet
