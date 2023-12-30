from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database, utils
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


# create user
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # hashing the password
    user.password = utils.hash(user.password)

    # save the user in the database
    new_user = models.User(**user.dict())  # this will give the sql statement to execute

    db.add(new_user)  # this will execute the sql statement
    db.commit()

    db.refresh(
        new_user
    )  # When you call session.refresh(new_user), it fetches the most recent
    # data from the database for the specified object (new_user in this
    # case) and updates the state of that object in the session.

    return new_user


# get user by id
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status=status.HTTP_404_NOT_FOUND, detail=f"User with {id} doesn't exists"
        )
    return user
