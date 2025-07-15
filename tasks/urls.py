from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:task_id>/', views.update_task_status, name='update_task'),
]
