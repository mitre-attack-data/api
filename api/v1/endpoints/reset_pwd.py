from datetime import timedelta
from fastapi import APIRouter, Request, HTTPException, status, Depends

from schemas.user import UserInDB
from settings import DefaultConfig

from services.auth.pwd_crypt_context import get_password_hash
from services.auth.user_validation import get_current_active_user, create_access_token
from services.email import EmailClient

from db.users import DataBaseUser


router = APIRouter()
config = DefaultConfig()


@router.post("/")
async def reset_pwd(request: Request, user: UserInDB = Depends(get_current_active_user)):

    db = DataBaseUser()
    
    user_request_data = await request.json()
    user_db = db.get_user(user_request_data.get('username', None))
    
    if(user_db is None):
        user_not_found_exception = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User not found.",
        )
        return user_not_found_exception
    
    # Redefine new password
    password_hash = get_password_hash(user_request_data.get('password', None))
    user.hashed_password = password_hash

    #Update user in the database
    user_inserted = db.update_one(user_data=user)
    if user_inserted:
        return HTTPException(
        status_code=status.HTTP_200_OK,
        detail="User updated successfully."
    )
    
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Unable to update user. Database error."
    )


# Email to user which request reset password 
@router.post("/reset-solicitation")
@router.post("/reset-solicitation/", include_in_schema=False)
async def request_reset_password(request: Request):

    db = DataBaseUser()
    
    user_request_data: dict = await request.json()
    user_db = db.get_user_by_email(user_request_data.get('email', None))
    
    if(user_db is None):
        user_not_found_exception = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )
        raise user_not_found_exception
    
    # Send hash to user email
    validation_code = user_db.hashed_password[len(user_db.hashed_password)-6:]

    message = f'\
        Aqui está seu código de validação <strong>{validation_code}</strong> para criar uma nova senha.<br>\
        Caso você não tenha solicita renovação de senha desconsirede este email.<br><br>\
        Equipe DreamTime<br><br><br>\
        __________________________________________________________________________________'

    conf = DefaultConfig()
    email = EmailClient(config=conf)
    email.reply(
        to=user_db.email,
        message_id='',
        subject='Request to Reset Password',
        message_text=message
    )
    
    return status.HTTP_200_OK


# Hash confirmation
@router.post("/reset-confirmation")
@router.post("/reset-confirmation/", include_in_schema=False)
async def hash_confirmation(request: Request):

    db = DataBaseUser()
    
    user_request_data: dict = await request.json()
    user_db = db.get_user(user_request_data.get('username', None))
    
    if(user_db is None):
        user_not_found_exception = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User not found.",
        )
        return user_not_found_exception

    # Validation
    validation_code = user_db.hashed_password[len(user_db.hashed_password)-6:]
    if validation_code == user_request_data.get('hash_validator', None):
        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user_db.username}, 
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}


    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid hash.",
    )
