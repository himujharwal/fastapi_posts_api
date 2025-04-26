
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):      # defineing what kind of response user will get. bcoz earlier it is all the data including id and other stuff now we are specifing which one should display to user
    id : int
    created_at: datetime
    owner_id : int

    class Config:           # so by defualt pydantic model read dict dtype but we use this one to tell that convert the sqlalchemy model(which is not dictinoary) to pydantic model
        # orm_mode = True        # this is depracted in V2
        from_attributes = True  # Updated in V2



class UserCreate(BaseModel):
    email : EmailStr
    password : str


class UserOut(BaseModel):
    id : int
    email : EmailStr

    class  Config:
        from_attributes = True



class UserLogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id :Optional[str] = None
    