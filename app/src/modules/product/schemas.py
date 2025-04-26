from pydantic import BaseModel
from enum import Enum
    

class Product(BaseModel):
    id: int
    name: str
    desc: str
    supplier: str
    listPrice: float

class ProductForSale(Product):
    salePrice: float