import uuid
from typing import Optional

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.common.db.base import Base


class Course(Base):
  __tablename__ = "courses"
  id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  title: Mapped[str] = mapped_column(String(255))
  description: Mapped[Optional[str]] = mapped_column(String(2000), nullable=True)
  is_published: Mapped[bool] = mapped_column(Boolean, default=False)

  enrollments: Mapped[list["Enrollment"]] = relationship(
    "Enrollment", back_populates="course", cascade="all, delete-orphan"
  )