from fastapi import APIRouter
from .. import models, schemas
from fastapi import Depends, status, Response, HTTPException
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

@router.get("/") # return all posts
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Posts).all()


@router.get("/{id}") # return a single post
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if(post == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return post


@router.post("/") # create a new post
def create_post(post: schemas.PostBase, db: Session = Depends(get_db)):
    new_post = models.Posts(title=post.title, content=post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # this returns the most recent added to post to posts model
    return new_post
    


@router.put("/{id}") # update a post
def update_post(id:int, updated_post: schemas.PostBase, db: Session = Depends(get_db)):
    post_query = db.query(models.Posts).filter(models.Posts.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")   
    print(post)
    post_query.update({"title": updated_post.title, "content": updated_post.content}, synchronize_session=False)
    db.commit()
    
    return post_query.first()


@router.delete("/{id}") # delete a post
def delete_post(id: int,  db: Session = Depends(get_db)):
    post_query = db.query(models.Posts).filter(models.Posts.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)