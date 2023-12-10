from django.urls import path, include
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('search/', views.search_feature, name='search-view'),
    path('<int:pk>/comment', views.AddCommentView.as_view(), name='addComment'),
    path('author/<str:username>', views.AuthorView.as_view(), name='authorFilter'),
    path('edit/<int:pk>/', views.UpdateStoryView.as_view(), name='updateStory'),
    path('edit/<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory'),
]
