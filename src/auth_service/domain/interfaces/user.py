import uuid
from typing import Protocol

from src.auth_service.domain.entities.user import UserCreateSchema, UserResponseSchema


class IUserRepository(Protocol):
    async def add(self, user: UserCreateSchema):
        pass

    async def users(self) -> list[UserResponseSchema]:
        pass

    async def detail(self, user_id: uuid.UUID) -> UserResponseSchema:
        pass

    async def get_by_id(self, user_id: uuid.UUID) -> UserResponseSchema:
        pass
