from src.auth_service.domain.interfaces.user import IUserRepository
from src.auth_service.infrastructure.database.models import User
from src.auth_service.infrastructure.security.password import PasswordHashed


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
    ) -> None:

        password_hash = self._hasher.hash(password)
        
        user = User(
            username=username,
            password=password_hash,
        )

        await self._user.add(user)



