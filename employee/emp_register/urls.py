from django.urls import path
from . import views

urlpatterns = [
    path('', views.empList, name='list'),
    path('emp-register', views.empCreate, name='register'),
    path('emp-update/<str:pk>', views.empUpdate, name="update"),
    path('emp-delete/<str:pk>', views.empDelete, name='delete')
]