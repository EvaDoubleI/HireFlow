from datetime import datetime

import bcrypt

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    BIGINT, TIMESTAMP, String, func
)

from . import Base

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
