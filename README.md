# Приложение для определения шаблона формы.

### Тестовое задание:

https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit?usp=sharing

Соискатель: Петров Александр

## Стек основных технологий:
- fastapi==0.104.1
- uvicorn==0.24.0.post1
- tinydb==4.8.0

Подробный стек в `requirements.txt`

## Как запустить?

### Вариант 1: в Docker-контейнере

#### 1. Клонировать репозиторий на локальную машину:
```bash
git clone git@github.com:AlexanderPAI/define_the_form.git
```

#### 2. Запустить приложение в Docker-контейнере

```bash
# В корневом каталоге приложения
docker-compose up --build
```
URL Веб-приложения - http://0.0.0.0:8000
___
### Вариант 2: без Docker-контейнера через виртуальное окружение

#### 1. Клонировать репозиторий на локальную машину:
```bash
git clone git@github.com:AlexanderPAI/define_the_form.git
```

#### 2. Перейти в корневой каталог приложения `define_the_form`, поднять виртуальное окружение, установить зависимости
```bash
# Перейти в корневой каталог приложения
cd define_the_form

# Поднять виртуальное окружение
python -m venv venv

# Активировать виртуальное окружение
# PowerShell(Windows)
.\venv\Script\activate
# Linux(Ubuntu)
source venv\bin\activate

# Обновить менеджер пакетов pip
(venv) python -m pip install --upgrade pip

# Установить зависимости
(venv) pip install -r requirements.txt
```

#### 3. Запустить приложение через `uvicorn`
```bash 
(venv) uvicorn app.main:app --host 0.0.0.0 --port 8000
```

URL Веб-приложения - http://0.0.0.0:8000

## Как работь?

В приложении имеется тестовая БД (tinyBD), наполненная тестовыми данными.
Расположение БД `app/services/db.json`

Путь расположения БД можно указать по своему усмотрению: в `app/services/db.py`:
```python
...
db = TinyDB('путь_БД')
...
```

#### Скрипт с тестовыми запросами

Скрипт с тестовыми запросами расположен `app/tests/test_requests.py`.
Результаты тестовых запросов из скрипта сохраняются путем логгирования в каталоге `app/tests/logs/`.

Запуск скрипта после запуска приложения:
```bash
#PowerShell(Windows)
python .\app\tests\test_requests.py
# Linux
python3 app/tests/test_requests.py
```

#### Примеры запросов
Для тестирования приложения рекомендуется использовать Postman или любое иное аналогичное приложение для работы с API. 

У приложения один единственный эндпоинт `/get_form`. Эндпоинт принимает только `post` запрос **без тела запроса**.

На эндпоинт `/get_form` передается форма в виде `query_parameters` по следующему шаблону:
```
http://0.0.0.0:8000/get_form?field1=value1&field2=value2
```

Например:

```
http://0.0.0.0:8000/get_form?Email=ya@ya.ru&Phone+Number=%2B7+901+132+22+12
```

Приложение осуществляет валидацию типа полей по их значению.
Поддерживает 4 типа значений:
- date - `DD.MM.YYYY`;
- phone - `+7 XXX XXX XX XX`;
- email - `xxxx@xxx.xx` или `xxxx@xxx.xxx.xx`
- text - без валидации.

После этого, в ответ возвращается либо список имен шаблонов из БД, которым форма соответствует, либо, если такого шаблона в БД нет, словарь вида `{'field1': 'type', 'field2': 'type'}`, содержащий поля формы и типы значений этих полей. 
