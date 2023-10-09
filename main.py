from fastapi import FastAPI
from routers import ne_router

app = FastAPI()

app.include_router(ne_router)
