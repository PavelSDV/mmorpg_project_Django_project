from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from .models import Post, Response
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.urls import reverse

# def get_user(): # если нужно все email вставить в поле кому
#     user_email = []
#     for user in User.objects.all():
#         user_email.append(user.email)
#     return user_email

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
            # post_url = reverse('post', args=[instance.id]) # можно и так получить url поста
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
            try:
                msg.send()
                print('Уведомление отправлено успешно')
            except Exception as e:
                print(f'Ошибка при отправке уведомления: {str(e)}')


@receiver(post_save, sender=Response)
def notify_user_response(sender, instance, created, **kwargs):
    if created:
        post_title = instance.postsResponse.title
        user_email = instance.postsResponse.user.email

        subject = 'Отклик на ваше объявление'
        text_content = f'На ваше объявление "{post_title}" поступил отклик.'

        msg = EmailMultiAlternatives(subject, text_content, 'newspaperss@yandex.ru', [user_email])

        html_content = '<p>На ваше объявление "<b>{}</b>" поступил отклик.</p>'.format(post_title)
        msg.attach_alternative(html_content, "text/html")

        try:
            msg.send()
            print('Уведомление отправлено успешно')
        except Exception as e:
            print(f'Ошибка при отправке уведомления: {str(e)}')
