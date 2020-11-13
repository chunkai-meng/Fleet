from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserProfileSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'display_name', 'groups')

