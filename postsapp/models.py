from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):
    tanks = 'TA'
    gila = 'GI'
    dd = 'DD'
    merchants = 'ME'
    guildmasters = 'GU'
    questgivers = 'QU'
    blacksmiths = 'BL'
    leatherworkers = 'LE'
    potions = 'PO'
    spell_masters = 'SP'

    CATEGORY_CHOICES = [
        (tanks, 'Танки'),
        (gila, 'Хилы'),
        (dd, 'ДД'),
        (merchants, 'Торговцы'),
        (guildmasters, 'Гилдмастеры'),
        (questgivers, 'Квестгиверы'),
        (blacksmiths, 'Кузнецы'),
        (leatherworkers, 'Кожевники'),
        (potions, 'Зельевары'),
        (spell_masters, 'Мастера заклинаний'),
    ]

    dataCreation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=tanks)
    contentText = models.TextField()
    contentImage = models.ImageField(upload_to=user_directory_path, blank=True)
    contentFile = models.FileField(upload_to=user_directory_path, blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}: {self.contentText[:123]}'

    def preview(self):
        return self.contentText[0:123] + '...'

    def email_preview(self):
        return f'{self.contentText[0:49]}...'

    def get_absolute_url(self):
        return f'/posts/{self.id}'


class Response(models.Model):
    dataResponse = models.DateTimeField(auto_now_add=True)
    userResponse = models.ForeignKey(User, on_delete=models.CASCADE)
    postsResponse = models.ForeignKey(Post, on_delete=models.CASCADE)
    contentResponse = models.TextField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Response by {self.userResponse.username} on {self.postsResponse.title}'
