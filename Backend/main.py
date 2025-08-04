from fastapi import FastAPI,Depends
import Schema
import model
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

def get_db():
    db=  sessionLocal()
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
def create_blog(user: Schema.User):
    return {"Blog": f"this is {user.username} with id as {user.id} and mail as {user.email}"}