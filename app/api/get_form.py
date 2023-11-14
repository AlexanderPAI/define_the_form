from fastapi import APIRouter, Request

from ..services.db import db
from ..services.classes import Form


router = APIRouter()


@router.post('/get_form')
def get_form(request: Request):
    """Эндпоинт для определения шаблона формы."""
    form = Form(request.query_params)
    template_names = form.find_template_in_db(db)
    if template_names:
        return template_names
    return form.get_form_template()
