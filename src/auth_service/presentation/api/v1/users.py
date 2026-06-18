from typing import List

from fastapi import APIRouter, Depends

from src.auth_service.application.use_cases.users import get_register_service, get_login_service
from src.auth_service.domain.entities.user import UserCreateSchema, UserResponseSchema, LoginResponseSchema, \
    UserLoginSchema
from src.auth_service.domain.services.login import LoginService
from src.auth_service.domain.services.register import RegisterService

api_v1_router = APIRouter()


@api_v1_router.post("/register", response_model=UserResponseSchema, status_code=201)
async def register_user(
        payload: UserCreateSchema,
        service: RegisterService = Depends(get_register_service),
):
    user = await service.register(username=payload.username, password=payload.password)
    return UserResponseSchema(user_id=user.id, username=user.username)


@api_v1_router.post("/login", response_model=LoginResponseSchema, status_code=200)
async def login(payload: UserLoginSchema,
                service: LoginService = Depends(get_login_service),
                ):
    result = await service.login(data=payload)
    return result
