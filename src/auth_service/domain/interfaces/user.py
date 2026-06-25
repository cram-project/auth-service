import uuid
from typing import Protocol, runtime_checkable

from src.auth_service.domain.entities.user import UserCreateSchema, UserResponseSchema, UpdateUserSchema
from src.auth_service.infrastructure.database.models import User


@runtime_checkable
class IUserRepository(Protocol):
    async def add(self, user: User):
        pass

    async def users(self) -> list[UserResponseSchema]:
        pass

    async def user_by_username(self, username: str):
        pass

    async def user_exists(self, username: str):
        pass

    async def get_user_by_id(self, id: uuid.UUID):
        pass

    async def update(self, user_id: uuid.UUID, user_data: UpdateUserSchema):
        pass