from django.urls import path
from firstapp import views

urlpatterns=[
    path('users',views.user,name='user'),
]
