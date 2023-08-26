from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import schemas,models
from .database import get_db
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

settings.jwt_expire_minutes = settings.jwt_expire_minutes

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.jwt_expire_minutes)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algo)
    return token

def verify_access_token(token:str, auth_error):
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algo,])
    except JWTError as jwt_error:
        raise auth_error
    id = payload.get("user_id")
    if id is None:
        raise auth_error
    token_data = schemas.TokenData(user_id=id)
    return token_data

def get_current_user(token:str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
    auth_error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})
    token_data = verify_access_token(token, auth_error)
    user = db.query(models.User).filter(models.User.id == token_data.user_id).first()
    return user
    