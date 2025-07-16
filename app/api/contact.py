from typing import Annotated

from fastapi import APIRouter
from fastapi import Form
from app.models.pydantic.contact import ContactForm

router = APIRouter()


@router.get("/message")
async def get_message():
    return {"message": "idi nahui"}


@router.post("/contact")
async def post_contact(data: Annotated[ContactForm, Form()]):
    print(data) #logging

    return {"success": True}