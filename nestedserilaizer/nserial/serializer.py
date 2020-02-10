from rest_framework import serializers
from nserial.models import Auther,Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class AutherSerializer(serializers.ModelSerializer):
    #while calling the data to show or ready only data we have created here
    books = BookSerializer(read_only=True,many=True)
    class Meta:
        model = Auther
        fields = "__all__"
