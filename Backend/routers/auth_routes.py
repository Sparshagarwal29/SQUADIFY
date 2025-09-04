from fastapi import APIRouter,Depends,HTTPException
from database import engine,get_db
from typing import Annotated
import model
import Authtoken
from hashing import Hash 
from sqlalchemy.orm import Session
import Schema
router = APIRouter()


db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/login",tags=["Auth"])
def userLogin(request: Schema.Login ,db: db_dependency,):
    user = db.query(model.User).filter(model.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found")
    if not Hash.verify_password(request.password,user.hashed_password): # type: ignore
        raise HTTPException(status_code=404, detail=f"INVALID PASSWORD")

    access_token = Authtoken.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}