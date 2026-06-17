
from src.auth_service.domain.interfaces.user import IUserRepository
from src.auth_service.infrastructure.security.password import PasswordHashed
from src.auth_service.infrastructure.security.token import JWTTokenProvider


class LoginService:
    def __init__(
            self,
            users: IUserRepository,
            hasher: PasswordHashed,
            tokens: JWTTokenProvider

    ) -> None:
        ...