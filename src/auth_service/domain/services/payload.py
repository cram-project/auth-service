from src.auth_service.infrastructure.database.models import User


def build_access_payload(user: User) -> dict:
    return {
        "id": str(user.id),
        "username": user.username,
        "is_staff": user.is_staff,
    }
