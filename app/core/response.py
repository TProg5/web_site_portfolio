from pydantic import BaseModel
from typing import Any, Optional


class APIResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[Any] = None