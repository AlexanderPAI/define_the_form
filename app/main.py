from fastapi import FastAPI

from app.api.get_form import router


app = FastAPI()


app.include_router(router)
