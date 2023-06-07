from django.urls import path
from .views import PostsList, PostsDetail, PostsAdd

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', PostsDetail.as_view(), name='new'),
    path('add/', PostsAdd.as_view(), name='add'),
]
