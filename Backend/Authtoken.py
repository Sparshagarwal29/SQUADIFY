from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from dotenv import load_dotenv
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
if not SECRET_KEY or not ALGORITHM:
    raise ValueError("SECRET_KEY and ALGORITHM must be set in .env")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM]) # type: ignore
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return{"email": email}
    except InvalidTokenError:
        raise credentials_exception