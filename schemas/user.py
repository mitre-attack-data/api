from typing import Optional
from pydantic import BaseModel


class UserInDB(BaseModel):
    name: Optional[str]
    full_name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str]
    disabled: Optional[bool] = False
    hashed_password: Optional[str]
