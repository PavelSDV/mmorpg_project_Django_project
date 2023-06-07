from django.urls import path
from .views import PostsList, PostsDetailView, PostsCreateView

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', PostsDetailView.as_view(), name='post'),
    path('create/', PostsCreateView.as_view(), name='create'),
]
