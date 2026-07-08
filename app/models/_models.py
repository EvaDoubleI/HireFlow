from datetime import datetime

import bcrypt

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import (
    BIGINT, TIMESTAMP, String, func
)


class Base(DeclarativeBase): pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BIGINT, autoincrement=True, primary_key=True)

    first_name: Mapped[str]
    second_name: Mapped[str]
    last_name: Mapped[str]

    phone_number: Mapped[str] = mapped_column(String(16), unique=True, nullable=False, index=True)
    _password_hash: Mapped[str]

    registration_date: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, plaintext_password: str):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plaintext_password.encode('utf-8'), salt)
        self._password_hash = hashed.decode('utf-8')

    def verify_password(self, plaintext_password: str) -> bool:
        return bcrypt.checkpw(
            plaintext_password.encode('utf-8'),
            self._password_hash.encode('utf-8')
        )

class Resume(Base):
    __tablename__ = "resume"

    id: ...
    user_id: ...

    title: ...
    about: ...
    salary: ...
    city: ...

class Education(Base):
    __tablename__ = "educations"

    id: ...
    resume_id: ...

    university: ...
    degree: ...
    start_date: ...
    end_date: ...

class Experience(Base):
    __tablename__ = "experiences"

    id: ...
    resume_id: ...

    company: ...
    position: ...
    description: ...

    start_date: ...
    end_date: ...

class Skill(Base):
    __tablename__ = "skills"

    id: ...
    name: ...

# TODO: Доделать Все таблицы и связать их между собой, так же сделать таблицу работодателя
