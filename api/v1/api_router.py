from fastapi import APIRouter

from .endpoints import auth
from .endpoints import sign_up
from .endpoints import reset_pwd
from .endpoints import user_data
from .endpoints import mitre


api_router = APIRouter()


api_router.include_router(
    router=auth.router, 
    prefix="/auth",
    tags=['Auth']
)

api_router.include_router(
    router=sign_up.router, 
    prefix="/sign-up",
    tags=['Sign-up']
)

api_router.include_router(
    router=reset_pwd.router, 
    prefix="/pwd",
    tags=['Reset password']
)

api_router.include_router(
    router=user_data.router, 
    prefix="/user",
    tags=['User']
)

api_router.include_router(
    router=mitre.router, 
    prefix="/mitre",
    tags=['Mitre ATT&CK']
)
