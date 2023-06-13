# from django.forms import ModelForm, BooleanField # Импортируем true-false поле
from django import forms
from django.forms import ModelForm, BooleanField, FileInput
from .models import Post, Response

# Создаём модельную форму
class PostForm(ModelForm):
    check_box = BooleanField(label='Подтверждаю')  # добавляем галочку или же true-false поле
    class Meta:
        model = Post
        fields = ['title', 'categoryType', 'contentText', 'contentImage', 'contentFile', 'check_box']  # не забываем включить галочку в поля, иначе она не будет показываться на странице!
        widgets = {
            'contentImage': FileInput(attrs={'accept': '.jpg'}),  # Указываем, что это поле для загрузки изображений
            'contentFile': FileInput(attrs={'accept': '.pdf,.doc,.docx,.txt'}),
        }

# class ResponseForm(forms.ModelForm):
class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['contentResponse']