from django.shortcuts import render
from rest_framework import generics
from nserial.models import Auther,Book
from nserial.serializer import AutherSerializer,BookSerializer

# Create your views here.

class AutherListView(generics.ListCreateAPIView):
    queryset = Auther.objects.all()
    serializer_class = AutherSerializer

class AutherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auther.objects.all()
    serializer_class = AutherSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
