from unicodedata import name
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='task-lsit'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create_task/', TaskCreate.as_view(), name='task-create'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task_delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),

]