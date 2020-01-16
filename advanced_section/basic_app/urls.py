from django.urls import path,re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns=[
    path('',views.SchoolListView.as_view(),name='list'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    re_path(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),
    re_path(r'^update/(?P<pk>[-\w]+)/$',views.SchoolUpdateView.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>[-\w]+)/$',views.SchoolDeleteView.as_view(),name='delete'),
]
