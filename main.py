from fastapi import FastAPI, Form, status, Depends, HTTPException, Request
import models
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import auth 
import mcq_generator
from fastapi.templating import Jinja2Templates
from icecream import ic


app = FastAPI()
app.include_router(auth.auth_router)
app.include_router(mcq_generator.router_gen_mcq)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.

# @app.post("/")
# async def process_login(username: str = Form(...), password: str = Form(...)):
#     # Use the check_valid_user function from your authentication route
#     user_credentials = {"username": username, "password": password}
#     try:
#         login_response = await auth.check_valid_user(user_credentials)
#         # If check_valid_user doesn't raise an exception, it means the credentials are valid
#         return {"message": "Login successful"}
#     except HTTPException as e:
#         # If check_valid_user raises an exception, handle the HTTPException
#         return {"message": f"Login failed: {e.detail}"}
    
#     # Do something with the username and password
#     return {"message": "Login successful"}