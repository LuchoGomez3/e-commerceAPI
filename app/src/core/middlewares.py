import json
import re
from typing import Any, Callable, Dict, Union

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


def camel_to_snake(name: str) -> str:
    """Convert camelCase string to snake_case."""
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def convert_dict_keys_to_snake_case(data: Any) -> Any:
    """Recursively convert all dictionary keys from camelCase to snake_case."""
    if isinstance(data, dict):
        return {camel_to_snake(k): convert_dict_keys_to_snake_case(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_dict_keys_to_snake_case(item) for item in data]
    return data


def contains_key_camel_case(data: Dict[str, Any]) -> bool:
    """
    Check if the data contains camelCase keys.
    This function checks all levels of the dictionary.

    Example:
    {'email': 'leacosta97@gmail.com', 'password': 'nAc!@JOiU%Dx!iiHZ', 'profile': {'name': 'string', 'last_name': 'string', 'gender': 'male', 'birthDate': '2025-04-11', 'location': 'string', 'pictureUrl': 'string'}, 'verification_code': '4077'}
    The function will return True because the key 'pictureUrl' is in camelCase.

    """
    for key, value in data.items():
        if re.match(r"^[a-z]+[A-Z]", key):
            return True
        if isinstance(value, dict):
            if contains_key_camel_case(value):
                return True
        elif isinstance(value, list):
            any_camel_case = any(contains_key_camel_case(item) for item in value)
            if any_camel_case:
                return True
    return False


async def camel_case_to_snake_case_middleware(request: Request, call_next: Callable) -> Any:
    """Middleware to convert camelCase request bodies to snake_case."""
    if request.method in ["POST", "PUT", "PATCH"]:
        try:
            body = await request.body()
            if body:
                json_body = json.loads(body)
                # Only convert if the body is in camelCase (check first level keys)
                if contains_key_camel_case(json_body):
                    converted_body = convert_dict_keys_to_snake_case(json_body)
                    # Replace the request body with the converted version
                    request._body = json.dumps(converted_body).encode()
        except json.JSONDecodeError:
            # If body is not JSON, continue without conversion
            pass

    response = await call_next(request)
    return response


async def custom_exception_handler(request: Request, exc: Union[HTTPException, Exception]) -> JSONResponse:
    print(f"Exception: {exc}")
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail, "status": exc.status_code},
        )
    # Handle other types of exceptions
    return JSONResponse(
        status_code=500,
        content={"error": str(exc), "status": 500},
    )
