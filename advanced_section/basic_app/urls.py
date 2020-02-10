from django.urls import path,re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns=[
    path('',views.SchoolListView.as_view(),name='list'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.SchoolDeleteView.as_view(),name='delete'),
    path('register/',views.Register,name='register'),
    path('login',views.user_login,name='user_login'),
    path('<int:pk>',views.SchoolDetailView.as_view(),name='detail'),
]
