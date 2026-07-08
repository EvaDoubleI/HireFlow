from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    BIGINT, DATE, String
)

from . import Base

class Resume(Base):
    __tablename__ = "resume"

    id: Mapped[int] = mapped_column(BIGINT, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT)

    title: Mapped[str] = mapped_column(String(64))
    about: Mapped[str] = mapped_column(String(300))
    salary: Mapped[float]
    city: Mapped[str]

class Education(Base):
    __tablename__ = "educations"

    id: Mapped[int] = mapped_column(BIGINT, autoincrement=True, primary_key=True)
    resume_id: ...

    university: Mapped[str]
    degree: Mapped[str]
    start_date: Mapped[datetime] = mapped_column(DATE)
    end_date: Mapped[datetime] = mapped_column(DATE)

class Experience(Base):
    __tablename__ = "experiences"

    id: Mapped[int] = mapped_column(BIGINT, autoincrement=True, primary_key=True)
    resume_id: ...

    company: Mapped[str]
    position: Mapped[str]
    description: Mapped[str]

    start_date: Mapped[datetime] = mapped_column(DATE)
    end_date: Mapped[datetime] = mapped_column(DATE)
