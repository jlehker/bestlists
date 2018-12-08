from rest_framework import serializers

from todovoodoo.core.models import TodoList, ListItem


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ("name", "frequency", "pub_id")


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ("description", "due_date", "pub_id")
