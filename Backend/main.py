from fastapi import FastAPI,Depends,HTTPException
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


@app.post("/User",status_code=201)  #this is someWhat similar to API (Application Programming Interface)
def create_User(user: Schema.User,db: db_dependency):
    newUser = model.User(username = user.username , email = user.email,hashed_password=user.hashed_password )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

@app.get("/User/{id}")
def get_User(id:int , db: db_dependency):
    user = db.query(model.User).filter(model.User.id== id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user

@app.delete("/User/{id}")
def delt_User(id:int,db: db_dependency):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    db.delete(user)
    db.commit()    
    # Instead of just {"ok": True}
    return {"message": f"User with id {id} deleted successfully"}





