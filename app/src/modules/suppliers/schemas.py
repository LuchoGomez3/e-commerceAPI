from pydantic import BaseModel
from enum import Enum
import uuid


class SupplierBase(BaseModel):
    name: str
    desc: str
    email: str
    
class SupplierCreate(SupplierBase):
    id: uuid.UUID