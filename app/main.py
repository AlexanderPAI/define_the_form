from fastapi import FastAPI, Request


app = FastAPI()


@app.post('/get_form')
def get_form(request: Request) -> dict[str, str]:
    """Эндпоинт для определения шаблона формы."""
    params = request.query_params
    return params
