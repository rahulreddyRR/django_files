from django.shortcuts import render

from rest_framework import serializers
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from core.models import students
from core.serializer import studentserilizer
from rest_framework.decorators import api_view

from rest_framework import generics,mixins

# Create your views here.
#ViewSets
class students_list(viewsets.ReadOnlyModelViewSet):
    queryset = students.objects.all()
    serializer_class = studentserilizer


"""
#GenericAPIView
class students_list(generics.ListCreateAPIView):
    queryset = students.objects.all()
    serializer_class = studentserilizer

class student_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = students.objects.all()
    serializer_class = studentserilizer"""

"""
#Mixins
class students_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = students.objects.all()
    serializer_class = studentserilizer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class student_details(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = students.objects.all()
    serializer_class = studentserilizer

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)

    def delete(self,request,pk):
        return self.destroy(request)
"""



"""
@api_view(['GET','POST'])
def students_list(request):
    if request.method == 'GET':
        student=students.objects.all()
        serializer = studentserilizer(student,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = studentserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def student_details(request,pk):
    try:
        student = students.objects.get(pk=pk)
    except students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        student=students.objects.all()
        serializer = studentserilizer(student,many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = studentserilizer(student,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
