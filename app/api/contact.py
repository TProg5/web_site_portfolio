from typing import Annotated

from fastapi import APIRouter
from fastapi import Form
from fastapi.responses import JSONResponse


from app.core.response import APIResponse
from app.models.pydantic.contact import ContactForm
from app.models.msg.message import MessageTemplates
from app.services.telegram_service import send_telegram_message

router = APIRouter(tags=["Contact"])


@router.post("/contact", description="Sends Contact Form to Telegam Bot", tags=["Contact"])
async def post_contact(
    data: Annotated[ContactForm, Form()],
) -> APIResponse:

    response = await send_telegram_message(
        message=MessageTemplates.contact_submission(data=data)
    )

    if response["success"]:

        return JSONResponse(
            content=APIResponse(
                success=True,
                message="Message answered"
            ).model_dump()
        )
    
    return JSONResponse(
        content=APIResponse(
            success=False,
            message=f"Error answer: {response.get("message", None)}"
        ).model_dump()
    )