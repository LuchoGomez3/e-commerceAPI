from fastapi import HTTPException


class UserNotFoundException(HTTPException):
    """Raised when a supplier is not found."""

    TYPE = "SUPPLIER_NOT_FOUND"

    def __init__(self) -> None:
        super().__init__(
            detail={"msg": "Supplier not found", "type": self.TYPE}, status_code=404
        )


class UserAlreadyExistsException(HTTPException):
    """Raised when a supplier already exist."""

    TYPE = "SUPPLIER_ALREADY_EXISTS"

    def __init__(self, field: str):
        self.field = field
        super().__init__(
            detail={
                "msg": f"Supplier with this {field} already exists",
                "type": self.TYPE,
            },
            status_code=400,
        )
