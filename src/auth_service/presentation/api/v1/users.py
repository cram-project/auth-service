from fastapi import APIRouter, Depends

from src.auth_service.application.use_cases.users import get_register_service
from src.auth_service.domain.entities.user import UserCreateSchema, UserResponseSchema
from src.auth_service.domain.services.register import RegisterService

api_v1_router = APIRouter()


@api_v1_router.post("/users", response_model=UserResponseSchema, status_code=201)
async def register_user(
        payload: UserCreateSchema,
        service: RegisterService = Depends(get_register_service),
):
    user = await service.register(username=payload.username, password=payload.password)
    return UserResponseSchema(user_id=user.id, username=user.username)

