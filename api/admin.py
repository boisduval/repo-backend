# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import TodoItem


@admin.register(TodoItem)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'description')
