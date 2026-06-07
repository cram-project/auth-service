from sqlalchemy import select

from src.auth_service.domain.entities.user import UserCreateSchema, UserResponseSchema
from src.auth_service.infrastructure.database.models import User
from src.auth_service.infrastructure.database.session import SessionDep


class UserRepository:
    def __init__(self, session: SessionDep):
        self._session = session

    async def add(self, user: UserCreateSchema):
        self._session.add(user)

        await self._session.commit()
        await self._session.refresh(user)

        return user

    async def users(self) -> list[UserResponseSchema]:
        query = select(User)

        result = await self._session.execute(query)

        return result.scalars().all()

