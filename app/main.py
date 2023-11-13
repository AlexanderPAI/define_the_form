import re

from fastapi import FastAPI, Request


class Form:
    """Класс формы."""

    def __init__(self, *args):
        self.__dict__.update(*args)

    def is_date(self, date: str) -> bool:
        """Валидатор поля 'Дата'."""
        regex_pattern = r'^\d{2}\.\d{2}\.\d{4}'
        if re.fullmatch(regex_pattern, date):
            return True
        return False

    def is_phone(self, phone: str) -> bool:
        """Валидатор поля 'Номер телефона'."""
        regex_pattern = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
        if re.fullmatch(regex_pattern, phone):
            return True
        return False

    def is_email(self, email: str) -> bool:
        """Валидатор поля 'Email'."""
        regex_pattern = r'(\w+[.-_])*\w+@\w+(\.[A-Z|a-z]{2,})+'
        if re.match(regex_pattern, email):
            return True
        return False

    def __str__(self):
        return 'Форма'


app = FastAPI()


@app.post('/get_form')
def get_form(request: Request) -> dict[str, str]:
    """Эндпоинт для определения шаблона формы."""
    params = request.query_params
    form = Form(params)
    return form.__dict__
