from pydantic import BaseModel
from enum import Enum
    

class ProductBase(BaseModel):
    name: str
    desc: str
    supplier: str
    listPrice: float

class ProductForSale(ProductBase):
    salePrice: float
    
class ProductWithId(ProductBase):
    id: int