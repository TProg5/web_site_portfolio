from pydantic import BaseModel
from pydantic import EmailStr, Field


class ContactForm(BaseModel):
    firstName: str
    username: str
    email: EmailStr
    inquiry: str
    message: str = Field(..., max_length=300) # limitation of the number of characters in a message at the Pydantic level
