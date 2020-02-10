from django.contrib import admin
from django.urls import path,include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students',views.students_list)


urlpatterns = [
    path('',include(router.urls)),
]
"""
urlpatterns = [
    path('studentlist/',views.students_list.as_view(),name='studentslist'),
    path('studentlist/<int:pk>',views.student_details.as_view(),name='studentsdetails'),
    path('admin/', admin.site.urls),
]
"""
