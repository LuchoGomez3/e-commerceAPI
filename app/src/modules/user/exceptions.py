from fastapi import HTTPException


class UserNotFoundException(HTTPException):
    """Raised when a user is not found."""

    TYPE = "USER_NOT_FOUND"

    def __init__(self) -> None:
        super().__init__(detail={"msg": "User not found", "type": self.TYPE}, status_code=404)


class UserAlreadyExistsException(HTTPException):
    """Raised when a user already exist."""
    
    TYPE = "USER_ALREADY_EXISTS"

    def __init__(self, field: str):
        self.field = field
        super().__init__(detail={"msg": f"User with this {field} already exists", "type": self.TYPE}, status_code=400)


class UserNotVerifiedException(HTTPException):
    """Raised when a user is not verified."""
    
    TYPE = "USER_NOT_VERIFIED"

    def __init__(self) -> None:
        super().__init__(detail={"msg": "User not verified", "type": self.TYPE}, status_code=400)
