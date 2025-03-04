from rest_framework import serializers
from .models import AndroidApp, UserTask

class AndroidAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = '__all__'

class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = '__all__'
