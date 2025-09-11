from pydantic import BaseModel, EmailStr
from typing import Union, Optional,List

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

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

class TeamMember(BaseModel):
    name: str
    role: str
    email: EmailStr
    contact:  str
    tech_stack: str 
    hobbies: Optional[str] = None
class TeamMembeResponse(BaseModel):
    id: int
    name:str
    role: str
    email:EmailStr
    contact: str
    tech_stack: str 
    hobbies: Optional[str] = None
    class Config:
        orm_mode = True

class CreateTeam(BaseModel):
    team_name: str 
    team_size: int
    members: List[TeamMember]
    
class showTeam(BaseModel):
    id: int
    team_name:str
    team_size: int
    creator_id: int
    members: List[TeamMembeResponse] = []
    class Config:
        orm_mode = True