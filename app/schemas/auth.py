from pydantic import BaseModel, field_validator

import phonenumbers

__all__ = ["UserRegistrate", "UserLogin"]

class UserRegistrate(BaseModel):
    name: str
    phone_number: str
    password: str

    @field_validator("phone_number")
    @classmethod
    def validate_phone(cls, value: str):
        try:
            parsed = phonenumbers.parse(value, "RU")
            if not phonenumbers.is_valid_number(parsed):
                raise ValueError

            return phonenumbers.format_number( parsed, phonenumbers.PhoneNumberFormat.E164 )
        except Exception:
            raise ValueError("Not correct phone number")

class UserLogin(BaseModel):
    phone_number: str
    password: str

