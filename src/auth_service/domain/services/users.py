from src.auth_service.infrastructure.database.repositories import UserRepository


class UserService:
    def __init__(self, users: UserRepository):
        self._users = users

