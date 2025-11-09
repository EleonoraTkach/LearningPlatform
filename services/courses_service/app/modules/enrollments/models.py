# services/courses_service/app/modules/enrollments/models.py
import uuid
from datetime import datetime, UTC
from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy import Enum as SAEnum, Boolean, String

from app.common.db.base import Base

class EnrollmentStatus(str, PyEnum):
    enrolled = "enrolled"
    active = "active"
    completed = "completed"
    cancelled = "cancelled"

class Enrollment(Base):
    __tablename__ = "enrollments"
    __table_args__ = (UniqueConstraint("user_id", "course_id", name="uq_enroll_user_course"),)

    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), index=True)  # ← ссылка на юзера по UUID
    course_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"), index=True)

    status: Mapped[EnrollmentStatus] = mapped_column(SAEnum(EnrollmentStatus, name="enrollment_status"), default=EnrollmentStatus.enrolled)
    progress: Mapped[int] = mapped_column(Integer, default=0)

    enrolled_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    course: Mapped["Course"] = relationship("Course", back_populates="enrollments")
