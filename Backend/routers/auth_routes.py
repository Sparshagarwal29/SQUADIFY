from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from typing import Annotated
import model
import Authtoken
from hashing import Hash 
from sqlalchemy.orm import Session
import Schema

router = APIRouter(tags=["Auth"])


db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/login",response_model=Schema.Token,tags=["Auth"])
def userLogin(request: Schema.Login ,db: db_dependency):
    user = db.query(model.User).filter(model.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found")
    if not Hash.verify_password(request.password, user.hashed_password):  # type: ignore
        raise HTTPException(status_code=401, detail=f"INVALID PASSWORD")

    access_token = Authtoken.create_access_token(
        data={"sub": user.email}
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token", response_model=Schema.Token, tags=["Auth"])
def login_for_access_token(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(model.User).filter(model.User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not Hash.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = Authtoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}