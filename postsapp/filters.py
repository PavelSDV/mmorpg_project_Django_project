from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Response


# создаём фильтр
class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {
            'dataCreation': ['gt'],  # позже какой-либо даты, что указал пользователь
            'title': ['icontains'], # мы хотим чтобы нам выводил заголовок хотя бы отдалённо похожее на то, что запросил пользователь
            'categoryType': ['exact'],  # должен точно совпадать тому, что указал пользователь
            'user': ['exact'],  # должен точно совпадать тому, что указал пользователь
        }

class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = {
            'dataResponse': ['gt'],
            'contentResponse': ['icontains'],
            'userResponse': ['exact'],
            'postsResponse__title': ['icontains'],
        }
