from fastapi import HTTPException


class ItemNotFoundException(HTTPException):
    """Raised when a product is not found."""

    TYPE = "PRODUCT_NOT_FOUND"

    def __init__(self) -> None:
        super().__init__(detail={"msg": "Product not found", "type": self.TYPE}, status_code=404)


class ItemAlreadyExistsException(HTTPException):
    """Raised when a product already exist."""
    
    TYPE = "PRODUCT_ALREADY_EXISTS"

    def __init__(self, field: str):
        self.field = field
        super().__init__(detail={"msg": f"Product with this {field} already exists", "type": self.TYPE}, status_code=400)
