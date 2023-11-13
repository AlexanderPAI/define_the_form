from fastapi import FastAPI, Request


class Form:
    """Класс формы."""

    def __init__(self, *args):
        self.__dict__.update(*args)

    def __str__(self):
        return 'Форма'


app = FastAPI()


@app.post('/get_form')
def get_form(request: Request) -> dict[str, str]:
    """Эндпоинт для определения шаблона формы."""
    params = request.query_params
    form = Form(params)
    return form.__dict__
