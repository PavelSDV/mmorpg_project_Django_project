from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from .models import Post
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.urls import reverse

# def get_user():
#     user_email = []
#     for user in User.objects.all():
#         user_email.append(user.email)
#     return user_email

# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=Post)
def notify_user_post(sender, instance, created, **kwargs):

        users = User.objects.exclude(id=instance.user_id)
        template = 'new_post.html'

        if created:
            subject = 'New post'
        else:
            subject = 'Edited post'

        for user in users:
            # user_email = get_user()
            # post_url = reverse('post', args=[instance.id])
            context = {
                'username': user.username,
                # 'post_url': post_url,
                'post': instance
            }

            html = render_to_string(template, context)

            msg = EmailMultiAlternatives(
                subject=subject,
                body='',
                from_email='newspaperss@yandex.ru',
                to=[user.email], # если каждому письмо отдельно
                # to=user_email, # одно письмо всем, все адреса в строке Кому
            )

            msg.attach_alternative(html, 'text/html', )
            msg.send()
