from fastapi import FastAPI, status, Depends, HTTPException
import models
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import auth 
import mcq_generator

app = FastAPI()
app.include_router(auth.auth_router)
app.include_router(mcq_generator.router_gen_mcq)

models.Base.metadata.create_all(bind=engine)
