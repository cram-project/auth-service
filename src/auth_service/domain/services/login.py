from sqlalchemy import select

from src.auth_service.domain.entities.user import UserLoginSchema
from src.auth_service.domain.interfaces.user import IUserRepository
from src.auth_service.infrastructure.database.models import User
from src.auth_service.infrastructure.security.password import PasswordHashed
from src.auth_service.infrastructure.security.token import JWTTokenProvider


class LoginService:
    def __init__(
            self,
            users: IUserRepository,
            hasher: PasswordHashed,
            tokens: JWTTokenProvider

    ) -> None:
        self._users = users
        self._hasher = hasher
        self._tokens = tokens

    async def login(self, data: UserLoginSchema):
        ...