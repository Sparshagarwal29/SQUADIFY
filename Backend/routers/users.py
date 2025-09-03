from fastapi import APIRouter,Depends,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
import model
import hashing
import Schema
from database import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/User",tags=["users"])
def all(db:db_dependency):
    user = db.query(model.User).all()
    return user

@router.get("/User/{id}", response_model = Schema.showUser,tags=["users"])
def get_User(id:int , db: db_dependency):
    user = db.query(model.User).filter(model.User.id== id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user

@router.post("/User",status_code=201,tags=["users"])  #this is someWhat similar to API (Application Programming Interface)
def create_User(user: Schema.UserCreate,db: db_dependency):
    existing_user = db.query(model.User).filter(model.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    newUser = model.User(username = user.username , email = user.email,hashed_password=hashing.Hash.get_password_hash(user.password)) # type: ignore
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

@router.delete("/User/{id}",status_code=204,tags=["users"])
def delt_User(id:int,db: db_dependency):
    deleteCount = db.query(model.User).filter(model.User.id == id).delete(synchronize_session=False)
    if deleteCount == 0:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    db.commit()    
    return "deleted"

@router.put("/User/{id}",tags=["users"])
def update(id:int , user: Schema.User , db: db_dependency):
    updateUser = db.query(model.User).filter(model.User.id == id)
    if not updateUser.first():
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    updateUser.update(user.dict()) # type: ignore
    db.commit()
    updated_user = db.query(model.User).filter(model.User.id == id).first()
    return updated_user  