from fastapi import FastAPI

from app.services.endpoints import router


app = FastAPI()


app.include_router(router)
