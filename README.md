# mmorpg_project

---------------------
В этом модуле мы наконец-то применим все полученные ранее знания о Django в одном цельном проекте: научимся проектировать архитектуру базы данных (моделей), разрабатывать шаблоны и представления для их отображения в разных контекстах, использовать события, отправлять письма и, что важнее всего, правильно связывать все элементы нашего проекта между собой.

→ Ваша работа над этим модулем будет очень похожа на работу разработчика-фрилансера, которому прислали техническое задание следующего содержания:

Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки.

Заранее спасибо!

--------------------------
-------------------------
Оценка задания

Павел, здравствуйте!
Работа оценена максимальными баллами по каждому критерию. 

Благодарю вас за качественно выполненную работу.
Вы отлично реализовали проект mmorpg_project согласно ТЗ, спроектировали модели Post, Response, создали статичные и динамичные представления, добавили авторизацию с подтверждением. 
Верно реализовали отправку писем на почту автору объявления при появлении отклика с помощью notify_user_response и автору отклика при приеме его сообщения в accept_response.

В целом отличная работа, так держать!
Проверку выполнила ментор Екатерина Попова
Если у вас остались вопросы, вы можете обратиться в канал  PWS_м_d13 в Пачке