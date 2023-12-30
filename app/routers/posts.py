from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(prefix="/posts", tags=["Posts"])


# get all posts
# for a user
@router.get("/", response_model=List[schemas.Post])
def get_posts(
    db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)
):
    print(current_user.id)
    posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")
    return posts


# create a post for a user
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# get post by id
@router.get("/{id}", response_model=schemas.PostOut)
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post = (
        db.query(models.Post)
        .filter(models.Post.id == id, models.Post.owner_id == current_user.id)
        .first()
    )

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found or does not belong to the current user",
        )

    return post


# delete post by id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )
    db.delete(post)
    db.commit()
    return "done"


# update post by id
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(
    id: int,
    request: schemas.Post,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )

    db.update(post)
    db.commit()
    # we can also do it like
    # post_query.delete(synchronize_session=False)

    return "updated"
