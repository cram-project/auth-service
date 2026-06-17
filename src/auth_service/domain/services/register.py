from src.auth_service.domain.interfaces.user import IUserRepository
from src.auth_service.infrastructure.database.models import User
from src.auth_service.infrastructure.security.password import PasswordHashed
from fastapi import HTTPException


class RegisterService:
    def __init__(
            self,
            user: IUserRepository,
            hasher: PasswordHashed,
    ):
        self._user = user
        self._hasher = hasher

    async def register(
            self,
            username: str,
            password: str,
    ) -> User:
        if await self._user.user_exists(username):
            raise HTTPException(status_code=400, detail="Username already registered")

        password_hash = self._hasher.hash(password)

        user = User(
            username=username,
            password_hash=password_hash,
        )

        return await self._user.add(user)