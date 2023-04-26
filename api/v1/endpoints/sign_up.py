from fastapi import APIRouter, Request, HTTPException, status

from schemas.auth import UserSignUp
from settings import DefaultConfig

from services.auth.pwd_crypt_context import get_password_hash
from db.users import DataBaseUser


router = APIRouter()
config = DefaultConfig()


@router.post("/")
async def sign_up_user(request: Request, user: UserSignUp):

    db = DataBaseUser()
    
    user_request_data: dict = await request.json()
    user_db = db.get_user(user_request_data.get('username', None))
    
    if(user_db is not None):
        already_exists_user_exception = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This user already exists.",
        )
        return already_exists_user_exception
    
    password_hash = get_password_hash(user_request_data.get('password', None))
    user.hashed_password = password_hash
    
    success_created = db.insert_one(user)
    if success_created:
        return HTTPException(
            status_code=status.HTTP_201_CREATED,
            detail="User created successfully.",
        )
    
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Unable to register user. Database error."
    ) 
