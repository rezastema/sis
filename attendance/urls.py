from django.urls import path
from .views import attendance_list, attendance_create

urlpatterns = [
    path('', attendance_list, name='attendance_list'),
    path('create/', attendance_create, name='attendance_create'),
]
