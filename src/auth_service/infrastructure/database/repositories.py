import uuid

from sqlalchemy import select
from src.auth_service.domain.entities.user import UserResponseSchema
from src.auth_service.infrastructure.database.models import User
from src.auth_service.infrastructure.database.session import SessionDep


class UserRepository:
    def __init__(self, session: SessionDep):
        self._session = session

    async def add(self, user: User):
        self._session.add(user)

        await self._session.commit()
        await self._session.refresh(user)

        return user

    async def users(self) -> list[UserResponseSchema]:
        query = select(User)

        result = await self._session.execute(query)

        return result.scalars().all()

    async def user_by_username(self, username: str):
        query = select(User).where(User.username == username)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def user_exists(self, username: str) -> bool:
        query = select(User).where(User.username == username)
        result = await self._session.execute(query)

        return result.scalar_one_or_none() is not None

    async def get_user_by_id(self, id: uuid.UUID) -> UserResponseSchema:
        query = select(User).where(User.id == id)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()