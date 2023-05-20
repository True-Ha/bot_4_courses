<h2 align="center">Fitness courses</h2>

How it works?  --> https://youtu.be/VgPHc9xsZ6A

### Описание проекта:
- Создание профиля, оплата через тг бота
- Права доступа к контенту только после оплаты
-
- Удобное создание плана тренировок через админ панель
- Восстановление пароля через почту, смена пароля на сайте
- Доступ к контенту с привязкой к IP
- Просмотр и обновление профиля юзера


**Стек**
- Python >= 3.11
- Django >= 4.1.7
- sqlite3

Установка

pip install req.txt

Старт

python manage.py runserver

## Разработка
#### 1) Поставить звездочку)
#### 2) Клонировать репозиторий
git clone https://github.com/True-Ha/fit_courses_bot.git

#### 3) Создать виртуальное окружение
cd core

python -m venv venv
#### 4) Активировать виртуальное окружение
Linux:
source venv/bin/activate
Windows:
./venv/Scripts/activate
#### 5) Устанавливить зависимости:
pip install -r req.txt
#### 6) Выполнить команду для выполнения миграций
python manage.py migrate
#### 7) Создать суперпользователя
python manage.py createsuperuser
#### 8) Запустить сервер
python manage.py runserver
#### 9) Ссылки
Сайт http://127.0.0.1:8000/

Админ панель http://127.0.0.1:8000/admin

