from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# Base models


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class UserBase(BaseModel):
    email: EmailStr


# Request models


class PostCreate(PostBase):
    # userid is set from token
    pass


class UserCreate(UserBase):
    password: str

class VoteCreate(BaseModel):
    post_id: int
    vote: bool

# Response models

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    user: User

    class Config:
        from_attributes = True

class PostAndVotes(BaseModel):
    post: Post = Field(validation_alias="Post")
    votes: int

    class Config:
        populate_by_name = True
        from_attributes = True

class Vote(BaseModel):
    user_id:int
    post_id:int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int]
