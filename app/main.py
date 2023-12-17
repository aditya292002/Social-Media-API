from fastapi import FastAPI
from .routers import posts
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)  # used to create the db tables if already doesn't exist

app = FastAPI()

app.include_router(posts.router)


@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}