from django.urls import path
from .views import PostsList, PostsDetailView, PostsCreateView, \
    PostsSearchView, PostsUpdateView, PostsDeleteView, ProfileView, \
    accept_response, delete_response


urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>/', PostsDetailView.as_view(), name='post'),
    path('search/', PostsSearchView.as_view(), name='search'),
    path('create/', PostsCreateView.as_view(), name='create'),
    path('create/<int:pk>/', PostsUpdateView.as_view(), name='create'),
    path('delete/<int:pk>/', PostsDeleteView.as_view(), name='delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('accept_response/<int:pk>/', accept_response, name='accept_response'),
    path('delete_response/<int:pk>/', delete_response, name='delete_response'),

]
