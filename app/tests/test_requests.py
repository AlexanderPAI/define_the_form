from requests import post
from json import loads

URL = 'http://127.0.0.1:8000/get_form?'

requests = [
    f'{URL}Phone=%2B7+903+123+45+12&Email=ya@ya.ru',
    f'{URL}name=Alex&Email=alex@mail.com&Phone=%2B7+911+222+34+22&Date=23.04.1990&Description=Test+Description',
    f'{URL}Date=01.03.2023&Description=Test+Description&Phone=%2B7+901+784+22=33&Email=info@stroydom.ru',
]

for request in requests:
    print(f'{"Запрос":-^150}')
    print(f'Тестовый запрос: {request}')
    response = post(request)
    print(f'Ответ: {loads(response.text)}')
