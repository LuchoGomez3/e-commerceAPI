import re
from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, field_validator


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

# ------------------ Perfiles ------------------
class ProfileBase(BaseModel):
    name: str = Field(min_length=1, max_length=32)
    last_name: str = Field(min_length=1, max_length=32)
    gender: Gender | None = None
    birth_date: date | None = None
    location: str | None = None
    picture_url: str | None = None


class ProfileCreate(ProfileBase):
    pass


class ProfileSchema(ProfileBase):
    id: int
    user_id: int

    model_config = {"from_attributes": True}


# ------------------ Usuarios ------------------
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str

    # Validate at least one uppercase, one lowercase, one number in pydantic v2
    @field_validator("password")
    def validate_password(cls, v):
        error_message = "Password must contain at least one uppercase letter, one lowercase letter, and one number"
        if not re.search(r"[A-Z]", v):
            raise ValueError(error_message)
        if not re.search(r"[a-z]", v):
            raise ValueError(error_message)
        if not re.search(r"[0-9]", v):
            raise ValueError(error_message)
        return v


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    profile: ProfileSchema

    model_config = {"from_attributes": True}


class UserSchema(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    profile: ProfileSchema

    model_config = {"from_attributes": True}


class UserUpdateRequest(BaseModel):
    profile: ProfileBase | None = None

    model_config = {"from_attributes": True}
