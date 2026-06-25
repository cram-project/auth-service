import uuid
from fastapi import HTTPException

from src.auth_service.domain.entities.user import UpdateUserSchema, UserResponseSchema
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


class UserUpdateService:
    def __init__(self, users: IUserRepository):
        self._users = users

    async def update(self, user_id: uuid.UUID, user_data: UpdateUserSchema) -> UserResponseSchema:

        if user_data.username is not None:
            existing_user = await self._users.user_by_username(user_data.username)

            if existing_user and existing_user.id != user_id:
                raise HTTPException(
                    status_code=409,
                    detail="This username is already taken."
                )

        updated_user = await self._users.update(user_id=user_id, user_data=user_data)

        if not updated_user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        return updated_user
