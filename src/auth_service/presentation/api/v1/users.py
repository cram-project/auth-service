import uuid

from fastapi import APIRouter, Depends
from src.auth_service.application.use_cases.users import get_register_service, get_login_service, get_user_service
from src.auth_service.domain.entities.user import UserCreateSchema, UserResponseSchema, LoginResponseSchema, \
    UserLoginSchema, UserPostCreateSchema, UserPayload
from src.auth_service.domain.services.login import LoginService
from src.auth_service.domain.services.register import RegisterService
from src.auth_service.domain.services.users import UserService
from src.auth_service.infrastructure.security.deps import get_current_user

api_v1_router = APIRouter()


@api_v1_router.post("/register", response_model=UserPostCreateSchema, status_code=201)
async def register_user(
        payload: UserCreateSchema,
        service: RegisterService = Depends(get_register_service),
):
    user = await service.register(username=payload.username, password=payload.password)

    return UserPostCreateSchema(user_id=user.id, username=user.username)


@api_v1_router.post("/login", response_model=LoginResponseSchema, status_code=200)
async def login(payload: UserLoginSchema,
                service: LoginService = Depends(get_login_service),
                ):
    result = await service.login(data=payload)
    return result


@api_v1_router.get("/users", response_model=list[UserResponseSchema])
async def get_users(service: UserService = Depends(get_user_service)):
    result = await service.list_users()

    return result


@api_v1_router.get("/users/{user_id}", response_model=UserResponseSchema)
async def detail_user(user_id: uuid.UUID ,service: UserService = Depends(get_user_service)):
    result = await service.detail(id=user_id)

    return result

@api_v1_router.get("/me", response_model=UserPayload)
async def me(current_user: UserPayload = Depends(get_current_user)):
    return current_user

