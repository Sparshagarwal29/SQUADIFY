from pydantic import BaseModel, EmailStr
from typing import Union, Optional

class Blog(BaseModel):  
    title: str
    body: str
    publication: Optional[int] = None



# class UserCreate(BaseModel):
#     username: str
#     email: EmailStr
#     password: str

# class User(BaseModel):
#     id: int
#     username: str
#     email: EmailStr

#     class Config:
#         orm_mode = True

# class Token(BaseModel):
#     access_token: str
#     token_type: str