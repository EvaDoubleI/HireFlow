from datetime import datetime

from pydantic import BaseModel, ConfigDict

__all__ = ["UserResponse"]

class UserResponse(BaseModel):
    id: int
    telegram_id: int

    name: str
    phone_number: str

    registration_date: datetime

    model_config = ConfigDict(from_attributes=True)
