from os import name
from django.urls import path
from .views import CreateAccountView, UpdateUserView, DeleteUserView
from .views import UserProfileView

app_name ='users'
urlpatterns = [    
        path('create-account/', CreateAccountView.as_view(), name='createAccount'),
        path('profile/<int:pk>/', UserProfileView.as_view(), name='userProfile'),
        path('edit/<int:pk>/', UpdateUserView.as_view(), name='updateUser'),
        path('edit/<int:pk>/delete', DeleteUserView.as_view(), name='deleteUser'),
    ]


