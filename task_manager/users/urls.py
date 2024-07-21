from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='user_create'),
]



# urlpatterns = [
#     path('', UserListView.as_view(), name='user_list'),
#     path('create/', UserCreateView.as_view(), name='user_create'),
#     path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
#     path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
# ]
