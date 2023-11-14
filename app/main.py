from fastapi import FastAPI, Request

from app.services.db import db
from app.services.classes import Form


app = FastAPI()


@app.post('/get_form')
def get_form(request: Request):
    """Эндпоинт для определения шаблона формы."""
    form = Form(request.query_params)
    template_names = form.find_template_in_db(db)
    if template_names:
        return template_names
    return form.get_form_template()
