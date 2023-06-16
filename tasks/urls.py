from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.list_tasks),
    path('new/', views.create_task, name='new_task' ),
    path('delete/<int:task_id>', views.delete_task, name='delete_task' )
]
