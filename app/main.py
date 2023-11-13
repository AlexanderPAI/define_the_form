from fastapi import FastAPI


app = FastAPI()


@app.post('/get_form')
def get_form() -> dict[str, str]:
    """Эндпоинт для определения шаблона формы."""
    return {'test': 'it is working'}
