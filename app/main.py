from fastapi import FastAPI

from .api.get_form import router


app = FastAPI()


app.include_router(router)
