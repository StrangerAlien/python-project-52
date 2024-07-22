from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='user_create'),
    path('', views.ReadUserView.as_view(), name='users_read'),
    path('<int:pk>/update', views.UpdateUserView.as_view(), name='user_update'),
    path('<int:pk>/delete', views.DeleteUserView.as_view(), name='user_delete'),
]
