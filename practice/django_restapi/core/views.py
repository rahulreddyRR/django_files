from django.shortcuts import render
from django.contrib.auth.models import User,Group
from core.serializer import studentserializer
from rest_framework import viewsets,generics,mixins
from core.models import students

# Create your views here.

class student_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = students.objects.all()
    serializer_class = studentserializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class student_details(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = students.objects.all()
    serializer_class = studentserializer

    def get(self,request,pk):
        return self.retrieve(request)
    def delete(self,request,pk):
        return self.destroy(request)
    def put(self,request,pk):
        return self.update(request)

"""
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""
