import re


class Form:
    """Класс формы."""

    REGEX_PATTERNS: dict[str, str] = {
        'date': r'^\d{2}\.\d{2}\.\d{4}',
        'phone': r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$',
        'email': r'(\w+[.-_])*\w+@\w+(\.[A-Z|a-z]{2,})+',
    }

    def __init__(self, *args):
        self.__dict__.update(*args)

    def _is_date(self, date: str) -> bool:
        """Валидатор поля 'Дата'."""
        if re.fullmatch(self.REGEX_PATTERNS['date'], date):
            return True
        return False

    def _is_phone(self, phone: str) -> bool:
        """Валидатор поля 'Номер телефона'."""
        if re.fullmatch(self.REGEX_PATTERNS['phone'], phone):
            return True
        return False

    def _is_email(self, email: str) -> bool:
        """Валидатор поля 'Email'."""
        if re.match(self.REGEX_PATTERNS['email'], email):
            return True
        return False

    def _field_type(self, value: str) -> str:
        """Определить тип поля по значению."""
        validators = (
            (self._is_date, 'date'),
            (self._is_phone, 'phone'),
            (self._is_email, 'email'),
        )

        default_type: str = 'text'

        for validator, field_type in validators:
            if validator(value):
                return field_type
        return default_type

    def get_form_template(self) -> dict[str, str]:
        """
        Преобразовать форму в шаблон. Возвращается словарь вида
        {'f_name1': 'value_type1', 'f_name2': 'value_type2' }.
        """
        form_template = {}
        for field, value in self.__dict__.items():
            form_template[field] = self._field_type(value)
        return form_template

    def find_template_in_db(self, db) -> list:
        """
        Найти в базе данных шаблон, соответствующий шаблону формы.
        Метод упрощен, так как используется tinyDB.
        При использовании "взрослой" БД, безусловно потребуется
        оптимизация запросов.
        """
        form_template = self.get_form_template()
        template_name_field: str = 'name'
        template_names: list = []
        for item in db:
            flag = False
            for field, field_type in item.items():
                if field != template_name_field:
                    if field in form_template.keys() and form_template[field] == field_type:
                        flag = True
                    else:
                        flag = False
                        break
            if flag:
                template_names.append(item[template_name_field])
        return template_names

    def __str__(self):
        return 'Форма'


form = Form({'name': 'Alex', 'email': 'ya@ya.ru'})
dct = form.get_form_template()
