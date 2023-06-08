from django.urls import path
from .views import PostsList, PostsDetailView, PostsCreateView, PostsSearchView

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', PostsDetailView.as_view(), name='post'),
    path('search/', PostsSearchView.as_view(), name='search'),
    path('create/', PostsCreateView.as_view(), name='create'),
]
