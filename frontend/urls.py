from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('taskstatus/<int:pk>', views.statusUpdate, name='taskstatus'),
    path('deletetask/<int:pk>', views.deleteTodo, name='deletetask'),
    path('createtodo/', views.create_todo, name='createtodo')
]