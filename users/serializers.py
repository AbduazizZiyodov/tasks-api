from typing import List

from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()

    def get_groups(self, obj: User) -> List[str]:
        return [
            group.name
            for group in obj.groups.all()
        ]

    class Meta:
        model = get_user_model()
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }
