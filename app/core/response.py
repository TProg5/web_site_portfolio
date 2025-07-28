from pydantic import BaseModel
from typing import Any, Optional


class APIResponse(BaseModel):
    """Wrapper for final API responses"""
    success: bool
    message: Optional[str] = None
    data: Optional[Any] = None