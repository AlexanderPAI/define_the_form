import re

from fastapi import FastAPI, Request


class Form:
    """Класс формы."""

    def __init__(self, *args):
        self.__dict__.update(*args)

    def __is_date(self, date: str) -> bool:
        """Валидатор поля 'Дата'."""
        regex_pattern = r'^\d{2}\.\d{2}\.\d{4}'
        if re.fullmatch(regex_pattern, date):
            return True
        return False

    def __is_phone(self, phone: str) -> bool:
        """Валидатор поля 'Номер телефона'."""
        regex_pattern = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
        if re.fullmatch(regex_pattern, phone):
            return True
        return False

    def __is_email(self, email: str) -> bool:
        """Валидатор поля 'Email'."""
        regex_pattern = r'(\w+[.-_])*\w+@\w+(\.[A-Z|a-z]{2,})+'
        if re.match(regex_pattern, email):
            return True
        return False

    def __field_type(self, value: str) -> str:
        """Определить тип поля по значению."""
        if self.__is_date(value):
            return 'date'
        if self.__is_phone(value):
            return 'phone'
        if self.__is_email(value):
            return 'email'
        return 'text'

    def get_form_template(self) -> dict:
        """
        Преобразовать форму в шаблон. Возвращается словарь вида
        {'f_name1': 'value_type1', 'f_name2': 'value_type2' }.
        """
        form_template = {}
        for key, value in self.__dict__.items():
            form_template[key] = self.__field_type(value)
        return form_template


app = FastAPI()


@app.post('/get_form')
def get_form(request: Request) -> dict[str, str]:
    """Эндпоинт для определения шаблона формы."""
    form = Form(request.query_params)
    form_template = form.get_form_template()
    return form_template
