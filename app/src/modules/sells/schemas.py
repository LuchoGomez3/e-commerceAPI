from pydantic import BaseModel
from enum import Enum
from datetime import date

from modules.product import ProductForSale

class Unity(Enum):
    UNITY = "UNITY"
    KG = "KG"
    GR = "GR"
    
class SaleBase(BaseModel):
    date: date
    products: list[ProductForSale]
    unity: Unity
    quantity: float
    
class SaleCreate(SaleBase):
    pass

class SaleWithId(SaleBase):
    id: int