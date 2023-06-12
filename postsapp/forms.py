# from django.forms import ModelForm, BooleanField # Импортируем true-false поле
from django.forms import ModelForm, BooleanField, FileInput, ClearableFileInput
from .models import Post

# Создаём модельную форму
class PostForm(ModelForm):
    check_box = BooleanField(label='Подтверждаю')  # добавляем галочку или же true-false поле
    class Meta:
        model = Post
        fields = ['title', 'categoryType', 'contentText', 'contentImage', 'contentFile', 'check_box']  # не забываем включить галочку в поля, иначе она не будет показываться на странице!
        widgets = {
            'contentImage': FileInput(attrs={'accept': '.jpg'}),  # Указываем, что это поле для загрузки изображений
            'contentFile': FileInput(attrs={'accept': '.pdf,.doc,.docx,.txt'}),
            # Указываем, что это поле для загрузки файлов
        }

        # widgets = {
        #     'contentImage': FileInput(attrs={'multiple': True}),
        #     'contentFile': FileInput(attrs={'multiple': True}),
        # }