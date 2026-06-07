import uuid
from datetime import datetime

from sqlalchemy import String, Boolean, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from src.auth_service.infrastructure.database.base import Base
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class User(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    username: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    password_hash: Mapped[str] = mapped_column(String(300), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    is_staff: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
