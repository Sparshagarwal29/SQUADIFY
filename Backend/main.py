from fastapi import FastAPI,Depends,HTTPException
from datetime import datetime, timedelta, timezone
import Schema
import hashing
from fastapi.middleware.cors import CORSMiddleware
import Authtoken
from hashing import Hash 
import model
from database import engine,get_db
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import EmailStr
from routers import users



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
    
db_dependency = Annotated[Session, Depends(get_db)]


app.include_router(users.router)


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
