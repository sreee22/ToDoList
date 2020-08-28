from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('task_update/<str:pk>/', views.updateTask, name="task_update"),
    path('task_delete/<str:pk>/', views.deleteTask, name="task_delete"),

]
