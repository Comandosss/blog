# Сайт "Blog by Django 4"

`Blog by Django 4` - веб-приложение разработанное с помощью веб-фреймворка Django 4 и Bootstrap 5. 

Разработан по курсу [Django 4 для начинающих](https://stepik.org/course/174634).

Сайт развернут на продакшн сервере с помощью Gunicorn, арендован VPS и домен: <http://alexlevkin.django-blog.ru>

## Возможности сайта

- Регистрация и авторизация пользователей по электронной почте или через Github/Google;
- Опция "Remember me", используя сессии и cookie; 
- Восстановление забытого пароля по почте;
- Редактирование личной информации и загрузка изображения аватара в личном кабинете;
- Полнотекстовый поиск постов по триграммному сходству;
- Отображение схожих постов по общим тегам;
- Возможность добавлять комментарии к постам с редактором Summernote;
- Рекомендация постов по электронной почте;
- Показ общего количества, последних добавленных и самых закоментированных постов;
- Удобная пагинация постов;
- Возможность редактирования постов, пользователей, комментариев к постам, и др. с панели администрирования;
- Карта сайта.

## Требования

- Python (версия 3.10.8)
- Django (версия 4.2.1)

## Установка и настройка

1. Клонируйте репозиторий приложения на вашу локальную машину:
```
git clone https://github.com/Comandosss/blog.git
```

2. Создайте виртуальное окружение
```
python -m venv env
```
3. Установите необходимые зависимости, используя pip:
```
pip install -r requirements.txt
```

4. Создайте файл `.env` в корневой папке проекта и впишите следующее:
```
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
```
6. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

7. Запустите сервер разработки Django:
```
python manage.py runserver
```

## Использование

1. Сперва необходимо создать пользователя, который будет иметь право управлять сайтом администрирования:
```
python manage.py createsuperuser
```

- введите имя пользователя, адрес электронной почты и пароль:

```
Username (leave blank to use 'admin'):
Email address:
Password:
Password (again):
```

2. Чтобы создать пост на сайте:
- нужно перейти на сайт администрирования:
  
```
http://127.0.0.1:8000/admin
```

- ввести свои логин и пароль суперпользователя и войти в систему:

![login_admin](https://github.com/Comandosss/blog/assets/49125444/878fb63b-e4ad-423f-85e8-4e611f5a0aed)

- нажать кнопку `Добавить` напротив `Posts`.

![add_posts](https://github.com/Comandosss/blog/assets/49125444/6280c0eb-2404-4506-b7db-c7b696db2f75)

- заполнить имеющиеся поля и нажать кнопку `СОХРАНИТЬ`:

![create_post](https://github.com/Comandosss/blog/assets/49125444/e5883133-fc66-4531-8ad0-004e8688fdfa)

- перейти на главную страницу и вы увидите, только что добавленный пост:

![blog_main](https://github.com/Comandosss/blog/assets/49125444/28e433e8-747f-4199-b360-5f92416d8224)

## Лицензия

[MIT License](LICENSE)
