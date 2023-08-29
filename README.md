# Сайт "Blog by Django 4"

[Blog by Django 4](http://alexlevkin.django-blog.ru/) - веб-приложение разработанное с помощью веб-фреймворка Django и Bootstrap 5. 
Разработан по курсу [Django 4 для начинающих](https://stepik.org/course/174634)

## Возможности сайта

- Регистрация и авторизация пользователей по электронной почте или через Github/Google;
- Добавлена опция "Remember me", используя сессии и cookie; 
- Восстановление забытого пароля по почте;
- Редактирование личной информации и загрузка изображения аватара в личном кабинете;
- Полнотекстовый поиск постов по триграммному сходству;
- Отображение схожих постов по числу имеющихся у них общих тегов;
- Система комментариев к постам с редактором Summernote;
- Реализация рекомендаций постов по электронной почте;
- Рекомендации схожих постов в посте;
- Показ общего количества постов, последних добавленных постов и самых закоментированных постов;
- Добавлена пагинация (3 поста на страницу);
- Есть админка;
- Карта сайта.

## Требования

- Python (версия 3.10.8)
- Django (версия 4.2.1)

## Установка и настройка

1. Клонируйте репозиторий приложения на вашу локальную машину:
```
https://github.com/Comandosss/blog.git
```

2. Создайте виртуальное окружение
```
python -m venv env
```
  
3. Установите необходимые зависимости, используя pip:
```
pip install -r requirements.txt
```

4. Создайте файл `.env` в корневой папке проекта. Впишите в .env следующее:

POSTGRES_DBNAME = 'Your name DB'

POSTGRES_USER = 'Your user'

POSTGRES_PASSWORD = 'Your password'

SECRET_KEY = 'Your secret key Django'

EMAIL_USER = 'Your email'

EMAIL_PASSWORD = 'Your password for external applications'

GITHUB_KEY = 'Your GitHub key'

GITHUB_SECRET = 'Your GitHub secret key'

GOOGLE_KEY = 'Your client ID'

GOOGLE_SECRET = 'Your client secret'

6. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

7. Запустите сервер разработки Django:
```
python manage.py runserver
```

## Использование

## Лицензия

[MIT License](LICENSE)
