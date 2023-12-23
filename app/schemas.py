from pydantic import BaseModel


class ShowPost(BaseModel):
    title: str
    content: str


class Post(BaseModel):
    title: str
    content: str
    owner_id: int

    class Config:
        orm_mode = True
