from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import models, database, utils, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):  # try this without using Depends() with oauthpasswordrequestform and see what happens
    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    # Valid user
    # create access token
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    # return the access token
    return {"access_token": access_token, "token_type": "bearer"}
