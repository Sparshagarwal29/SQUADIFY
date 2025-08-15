from fastapi import FastAPI,Depends,HTTPException
from datetime import datetime, timedelta, timezone
import Schema
import hashing
from fastapi.middleware.cors import CORSMiddleware
import Authtoken
from hashing import Hash 
import model
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import EmailStr


app = FastAPI()
model.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db= SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Database error: {e}")
        db.rollback()
        raise 
    finally:
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/User",status_code=201,tags=["users"])  #this is someWhat similar to API (Application Programming Interface)
def create_User(user: Schema.UserCreate,db: db_dependency):
    newUser = model.User(username = user.username , email = user.email,hashed_password=hashing.Hash.get_password_hash(user.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


@app.get("/User/{id}", response_model = Schema.showUser,tags=["users"])
def get_User(id:int , db: db_dependency):
    user = db.query(model.User).filter(model.User.id== id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user
    
@app.get("/User",tags=["users"])
def all(db:db_dependency):
    user = db.query(model.User).all()
    return user

@app.delete("/User/{id}",status_code=204,tags=["users"])
def delt_User(id:int,db: db_dependency):
    deleteCount = db.query(model.User).filter(model.User.id == id).delete(synchronize_session=False)
    if deleteCount == 0:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    db.commit()    
    return "deleted"

@app.put("/User/{id}",tags=["users"])
def update(id:int , user: Schema.User , db: db_dependency):
    updateUser = db.query(model.User).filter(model.User.id == id)
    if not updateUser.first():
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    updateUser.update(user.dict())
    db.commit()
    updated_user = db.query(model.User).filter(model.User.id == id).first()
    return updated_user  



@app.post("/login",tags=["Auth"])
def userLogin(request: Schema.Login ,db: db_dependency,):
    user = db.query(model.User).filter(model.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found")
    if not Hash.verify_password(request.password,user.hashed_password):
        raise HTTPException(status_code=404, detail=f"INVALID PASSWORD")

    access_token = Authtoken.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
