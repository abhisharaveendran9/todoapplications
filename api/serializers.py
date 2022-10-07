from rest_framework.serializers import ModelSerializer
from todoapp.models import Todos
from rest_framework import serializers

class TodoSerializer(ModelSerializer):
    user=serializers.CharField(read_only=True)

    class Meta:
        model=Todos
        fields="__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        return Todos.objects.create(**validated_data,user=user)
