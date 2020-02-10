from rest_framework import serializers
from core.models import students

class studentserilizer(serializers.ModelSerializer):
    class Meta:
         model = students
         fields= ['name','score']
