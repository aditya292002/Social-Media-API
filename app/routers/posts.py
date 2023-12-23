from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List


from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/posts", tags=["Posts"])


# get all posts
@router.get("/", response_model=List[schemas.ShowPost])
def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


# create a post
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(request: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(title=request.title, content=request.content, owner_id=1)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# get post by id
@router.get("/{id}", status_code=200, response_model=schemas.ShowPost)
def get_post(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    return post


# delete post by id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return "done"


# update post by id
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, request: schemas.Post, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    post.update(request)
    db.commit()
    return "updated"
