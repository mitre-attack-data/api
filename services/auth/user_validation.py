from typing import Optional
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from schemas.user import UserInDB
from services.auth.pwd_crypt_context import verify_password
from settings import DefaultConfig
from db.users import DataBaseUser


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")   
config = DefaultConfig()



def authenticate_user(username: str, password: str):
    db = DataBaseUser()
    user = db.get_user(username)
    
    if not user:
        return False
    
    if not verify_password(password, user.hashed_password):
        return False
    
    return user



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims=to_encode, 
        key=config.SECRET_KEY, 
        algorithm=config.ALGORITHM
    )
    
    return encoded_jwt



async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            token=token, 
            key=config.SECRET_KEY, 
            algorithms=[config.ALGORITHM]
        )
        username: str = payload.get("sub")
        
        if username is None:
            raise credentials_exception
    
    except JWTError:
        raise credentials_exception
    
    db = DataBaseUser()
    user = db.get_user(username)
    
    if user is None:
        raise credentials_exception
    
    return user



async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
