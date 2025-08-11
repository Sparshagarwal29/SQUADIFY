from pydantic import BaseModel, EmailStr
from typing import Union, Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str 

class User(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str 

class showUser(BaseModel):
    username: str
    email: EmailStr
    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str 

# class Token(BaseModel):
#     access_token: str
#     token_type: str