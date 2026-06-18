import uuid
from fastapi import HTTPException
from src.auth_service.domain.interfaces.user import IUserRepository


class UserService:
    def __init__(self, users: IUserRepository):
        self._users = users

    async def list_users(self):
        users = await self._users.users()

        return users

    async def detail(self, id: uuid.UUID):
        user = await self._users.get_user_by_id(id)

        if not user:
            raise HTTPException(detail="User not found", status_code=404)

        return user
