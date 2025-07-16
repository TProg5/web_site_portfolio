from pydantic import BaseModel
from pydantic import EmailStr, Field


class ContactForm(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    inquiry: str
    message: str = Field(..., max_length=300) 
    #ограничение количества символов в сообщении на уровне Pydantic
