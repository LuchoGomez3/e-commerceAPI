import uuid
from enum import Enum

from pydantic import BaseModel


class SupplierBase(BaseModel):
    name: str
    desc: str
    email: str


class SupplierCreate(SupplierBase):
    id: uuid.UUID
