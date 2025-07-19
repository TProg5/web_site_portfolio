from typing import Annotated

from fastapi import APIRouter
from app.core.response import APIResponse

from fastapi import Form
from app.models.pydantic.contact import ContactForm

from app.services.telegram_service import send_telegram_message
from app.models.msg.message import MessageTemplates

router = APIRouter()


@router.post("/contact")
async def post_contact(
    data: Annotated[ContactForm, Form()],
) -> APIResponse:

    response = await send_telegram_message(
        message=MessageTemplates.contact_submission(data=data)
    )

    if response["status"]:
        return APIResponse(
            success=True,
            message="Message answered"
        )
    
    return APIResponse(
        success=False,
        message=f"Error answer: {response.get("message", None)}"
    )