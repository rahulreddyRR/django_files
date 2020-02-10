
from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns=[
    path('',views.student_list.as_view()),
    path('studentdetails/<int:pk>/',views.student_details.as_view())
]








"""from core.views import UserViewset,GroupViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',UserViewset)
router.register('groups',GroupViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]"""
