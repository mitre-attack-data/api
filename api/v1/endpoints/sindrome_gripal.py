# from fastapi import APIRouter, Depends, status, HTTPException

# from schemas.sindrome_gripal import Query
# from schemas.auth import User
# from settings import DefaultConfig

# from services.auth.user_validation import get_current_active_user
# from services.elasticserach_api import ElasticHttpSearch


# router = APIRouter()
# config = DefaultConfig()



# # async def get_data(query: Query, _: User = Depends(get_current_active_user)):
# @router.post("/casos/", status_code=status.HTTP_200_OK)
# async def get_data(query: Query):
    
#     es = ElasticHttpSearch()
#     data, status_code = es.req(uf=query.uf, municipio=query.municipio)

#     if status_code in [200, 201, 202]:
#         return data

#     return HTTPException(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         detail=data,
#     )
