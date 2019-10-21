from rest_framework import serializers
from .models import TodoItem


class TodoItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'state', 'description')
