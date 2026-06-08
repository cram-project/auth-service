import uuid


class UserPayload:
    user_id: uuid.UUID
    username: str


class UserCreateSchema:
    username: str
    password: str


class UserResponseSchema:
    user_id: uuid.UUID
    username: str
    password: str
