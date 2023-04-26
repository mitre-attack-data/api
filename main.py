from fastapi import FastAPI
from api.v1.api_router import api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def heathcheck():
    return {"message": "It's working."}


app.include_router(api_router, prefix='/api/v1')
