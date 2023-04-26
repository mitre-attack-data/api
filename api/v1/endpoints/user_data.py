from fastapi import APIRouter, Depends

from schemas.user import UserInDB
from settings import DefaultConfig

from services.auth.user_validation import get_current_active_user



router = APIRouter()
config = DefaultConfig()



@router.get("/me/")
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    data = current_user.dict()
    del data['hashed_password']
    return data
