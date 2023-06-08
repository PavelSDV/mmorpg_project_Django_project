from django.urls import path
from .views import PostsList, PostsDetailView, PostsCreateView, PostsSearchView, PostsUpdateView, PostsDeleteView

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', PostsDetailView.as_view(), name='post'),
    path('search/', PostsSearchView.as_view(), name='search'),
    path('create/', PostsCreateView.as_view(), name='create'),
    path('create/<int:pk>/', PostsUpdateView.as_view(), name='create'),
    path('delete/<int:pk>/', PostsDeleteView.as_view(), name='delete'),
]
