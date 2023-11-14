from fastapi import FastAPI, Request

from app.services.endpoints import router


app = FastAPI()


app.include_router(router)
