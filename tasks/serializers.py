from rest_framework import serializers

from .models import Task

from users.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields: str = "__all__"
        extra_kwargs = {'user': {'required': True}}


class TaskListSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj: Task) -> dict:
        return UserSerializer(
            obj.user
        ).data

    class Meta:
        model = Task
        fields: str = "__all__"
