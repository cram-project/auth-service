from fastapi import Depends

from src.auth_service.domain.services.register import RegisterService
from src.auth_service.infrastructure.database.repositories import UserRepository
from src.auth_service.infrastructure.database.session import SessionDep
from src.auth_service.infrastructure.security.password import PasswordHashed

_hasher = PasswordHashed()


def get_password_hasher() -> PasswordHashed:
    return _hasher


def get_user_repository(session: SessionDep) -> UserRepository:
    return UserRepository(session)


def get_register_service(
    user: UserRepository = Depends(get_user_repository),
    hasher: PasswordHashed = Depends(get_password_hasher),

) -> RegisterService:
    return RegisterService(
        user=user,
        hasher=hasher,
    )