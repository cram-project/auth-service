import uuid

from pydantic import BaseModel


class UserPayload(BaseModel):
    user_id: uuid.UUID
    username: str


class UserCreateSchema(BaseModel):
    username: str
    password: str


class UserResponseSchema(BaseModel):
    user_id: uuid.UUID
    username: str


class UserLoginSchema(BaseModel):
    username: str
    password: str