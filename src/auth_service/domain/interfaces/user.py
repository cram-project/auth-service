import uuid
from typing import Protocol, runtime_checkable

from src.auth_service.domain.entities.user import UserCreateSchema, UserResponseSchema
from src.auth_service.infrastructure.database.models import User


@runtime_checkable
class IUserRepository(Protocol):
    async def add(self, user: User):
        pass

    async def users(self) -> list[UserResponseSchema]:
        pass

    async def detail(self, user_id: uuid.UUID) -> UserResponseSchema:
        pass

    async def get_by_id(self, user_id: uuid.UUID) -> UserResponseSchema:
        pass
