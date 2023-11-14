from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status # to return correct status code back to user
from database import SessionLocal
from models import Users
from passlib.context import CryptContext

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CreateUserRequest(BaseModel):
    username:str
    password:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@auth_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        hashed_password = bcrypt_context.hash(create_user_request.password),
    )
    
    db.add(create_user_model)
    db.commit()
    

# check valid user
@auth_router.post("/login")
async def check_valid_user(db: db_dependency,
                      create_user_request: CreateUserRequest, status_code=status.HTTP_200_OK):

    user = db.query(Users).filter_by(username=create_user_request.username).first()
    if not user or not bcrypt_context.verify(create_user_request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
        
    else:
        return {"status": "Valid user"}