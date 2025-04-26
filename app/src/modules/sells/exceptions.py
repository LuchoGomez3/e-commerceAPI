from fastapi import HTTPException


class UserNotFoundException(HTTPException):
    """Raised when a sell is not found."""

    TYPE = "SELL_NOT_FOUND"

    def __init__(self) -> None:
        super().__init__(detail={"msg": "Sell not found", "type": self.TYPE}, status_code=404)


class UserAlreadyExistsException(HTTPException):
    """Raised when a user already exist."""
    
    TYPE = "SELL_ALREADY_EXISTS"

    def __init__(self, field: str):
        self.field = field
        super().__init__(detail={"msg": f"Sell with this {field} already exists", "type": self.TYPE}, status_code=400)

