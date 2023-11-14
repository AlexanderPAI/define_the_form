import re


class Form:
    """Класс формы."""

    def __init__(self, *args):
        self.__dict__.update(*args)

    @staticmethod
    def __is_date(date: str) -> bool:
        """Валидатор поля 'Дата'."""
        regex_pattern = r'^\d{2}\.\d{2}\.\d{4}'
        if re.fullmatch(regex_pattern, date):
            return True
        return False

    @staticmethod
    def __is_phone(phone: str) -> bool:
        """Валидатор поля 'Номер телефона'."""
        regex_pattern = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
        if re.fullmatch(regex_pattern, phone):
            return True
        return False

    @staticmethod
    def __is_email(email: str) -> bool:
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

    def find_template_in_db(self, db) -> list:
        """
        Найти в базе данных шаблон, соответствующий шаблону формы.
        Метод упрощен, так как используется tinyDB.
        При использовании "взрослой" БД, безусловно потребуется
        оптимизация запросов.
        """
        form_template = self.get_form_template()
        template_names = []
        for item in db:
            flag = False
            for key, value in item.items():
                if key != 'name':
                    if key in form_template.keys() and form_template[key] == value:
                        flag = True
                    else:
                        flag = False
                        break
            if flag:
                template_names.append(item['name'])
        return template_names

    def __str__(self):
        return 'Форма'