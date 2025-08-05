from fastapi import FastAPI,Depends
import Schema
import model
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

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


@app.get("/")
def read_root():
    return {"Hello": "World mai hu giyan"}


@app.post("/User")
def create_User(user: Schema.User,db: db_dependency):
    newUser = model.User(username = user.username , email = user.email,hashed_password=user.hashed_password )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
