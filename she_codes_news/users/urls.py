from os import name
from django.urls import path
from .views import CreateAccountView, UpdateUserView
from .views import UserProfileView

app_name ='users'
urlpatterns = [    
        path('create-account/', CreateAccountView.as_view(), name='createAccount'),
        path('profile/<int:pk>/', UserProfileView.as_view(), name='userProfile'),
        # path('profile/<str:username>/', UserProfileView.as_view(), name='userProfile')
        # path('<int:pk>/', views.StoryView.as_view(), name='story'),
        path('update/<int:pk>/', UpdateUserView.as_view(), name="updateUser")

    ]


