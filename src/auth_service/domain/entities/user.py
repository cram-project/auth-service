import uuid


class UserPayload:
    id: uuid.UUID
    username: str
    password: str


class UserCreateSchema:
    username: str
    password: str


class UserResponseSchema:
    id: uuid.UUID
    username: str
    password: str
