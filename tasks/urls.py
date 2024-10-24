from django.urls import path
from . import views

urlpatterns = [
    # path('t/', views.tasks, name='tasks'),
    # path('u/', views.users, name='users'),
    # path('', views.home, name='home'),
    path('', views.task_list, name="task_list"),
    path('<int:id>/', views.task_list, name="task_list"),
]