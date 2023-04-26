from fastapi import APIRouter, Depends, status, HTTPException, Request

from services.mitre import Mitre
from db.mitre import DataBaseMitre
from settings import DefaultConfig
from services.auth.user_validation import get_current_active_user


router = APIRouter()
config = DefaultConfig()


@router.post("/generate-tactics")
@router.post("/generate-tactics/", include_in_schema=False)
async def generate_tactics(request: Request):
    
    mitre_client = Mitre()
    mitre_db = DataBaseMitre(collection='tactics')

    data_tactics = mitre_client.get_all_tactics()
    success = mitre_db.insert_many(data=data_tactics)

    print(f"Sucesso: {success}")
    
    return HTTPException(
        status_code=status.HTTP_200_OK,
        detail='ok',
    )



@router.get("/all-tactics")
@router.get("/all-tactics/", include_in_schema=False)
async def list_tactics(request: Request):
    
    mitre_db = DataBaseMitre(collection='tactics')
    all_tactics = mitre_db.list_tactics()
    return all_tactics
