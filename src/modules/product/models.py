from pydantic import Field, validator
from enum import Enum
from sqlmodel import SQLModel, Relationship
from typing import Optional

class SuppliersName(str, Enum):
    SERIN = "SERIN"
    FERGRALPAZ= "FERRETERA GRAL PAZ"
    LEKONS = "LEKONS"
    LALILY = "LALILY"
    AMANCO = "AMANCO"
    CANTERA = "CANTERA EL ALTO"

class SupplierBase(SQLModel):
    name: str = Field(min_length=3, max_length=100, description="Nombre del proveedor")
    desc: Optional[str] = Field(default=None, max_length=500, description="Descripción del proveedor")
    address: str = Field(min_length=5, max_length=200, description="Dirección del proveedor")
    phone: str = Field(description="Número de teléfono del proveedor")

    @validator("phone")
    def validate_phone(cls, value):
        # Aquí podrías agregar una validación más robusta para el formato del teléfono
        if not value.isdigit():
            raise ValueError("El número de teléfono debe contener solo dígitos")
        return value

class Supplier(SupplierBase, table=True):
    id: int = Field(default=None, primary_key=True)

class ProductBase(SQLModel):
    name: str = Field(min_length=3, max_length=100, description="Nombre del producto")
    desc: Optional[str] = Field(default=None, max_length=500, description="Descripción del producto")
    supplier: SuppliersName = Field(description="Proveedor del producto")
    listPrice: int = Field(gt=0, description="Precio de lista del producto")

class ProductForSale(ProductBase):
    salePrice: int = Field(gt=0, description="Precio de venta del producto")

    @validator("salePrice")
    def validate_sale_price(cls, value, values):
        if "listPrice" in values and value <= values["listPrice"]:
            return value
        raise ValueError("El precio de venta debe ser mayor que el precio de lista")

class Product(ProductBase, table=True):
    id: int = Field(default=None, primary_key=True)