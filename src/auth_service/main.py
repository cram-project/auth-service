from fastapi import FastAPI
from src.auth_service.presentation.api.v1.users import api_v1_router

app = FastAPI()

app.include_router(api_v1_router, prefix="/auth")
