from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.core.templates import templates

router = APIRouter()


@router.get("/main", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )
