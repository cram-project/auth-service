from sqlalchemy import select
from fastapi import HTTPException
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

        return HTTPException(status_code=201, detail="User added")

    async def users(self) -> list[UserResponseSchema]:
        query = select(User)

        result = await self._session.execute(query)

        return result.scalars().all()

    async def user_by_username(self, username: str):
        query = select(User).where(User.username == username)
        result = await self._session.execute(query)

        return result.scalar_one()
