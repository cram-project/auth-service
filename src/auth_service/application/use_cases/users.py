from fastapi import Depends

from src.auth_service.domain.services.login import LoginService
from src.auth_service.domain.services.refresh_service import RefreshService
from src.auth_service.domain.services.register import RegisterService
from src.auth_service.domain.services.users import UserService
from src.auth_service.infrastructure.database.repositories import UserRepository
from src.auth_service.infrastructure.database.session import SessionDep
from src.auth_service.infrastructure.security.password import PasswordHashed
from src.auth_service.infrastructure.security.token import JWTTokenProvider

_hasher = PasswordHashed()
_tokens = JWTTokenProvider()


def get_password_hasher() -> PasswordHashed:
    return _hasher


def get_user_repository(session: SessionDep) -> UserRepository:
    return UserRepository(session)


def get_token_provider() -> JWTTokenProvider:
    return _tokens


def get_register_service(
        user: UserRepository = Depends(get_user_repository),
        hasher: PasswordHashed = Depends(get_password_hasher),

) -> RegisterService:
    return RegisterService(
        user=user,
        hasher=hasher,
    )


def get_login_service(
        users: UserRepository = Depends(get_user_repository),
        hasher: PasswordHashed = Depends(get_password_hasher),
        tokens: JWTTokenProvider = Depends(get_token_provider),
) -> LoginService:
    return LoginService(
        users=users,
        hasher=hasher,
        tokens=tokens,
    )


def get_user_service(
        users: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(
        users=users,
    )


def get_refresh_service(
        users: UserRepository = Depends(get_user_repository),
        tokens: JWTTokenProvider = Depends(get_token_provider)
) -> RefreshService:
    return RefreshService(
        users=users,
        tokens=tokens
    )
