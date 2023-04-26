from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserSignUp(BaseModel):
    name: str
    full_name: str
    email: str
    username: str
    password: str
    disabled:  Optional[str]
    hashed_password: Optional[str]


class UserPwdReset(BaseModel):
    email: str
    hashed_password: Optional[str]
