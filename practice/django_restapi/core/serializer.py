from rest_framework import serializers
from django.contrib.auth.models import User,Group
from core.models import students

class studentserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = students
        fields = ['name','marks']


"""class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']
"""
