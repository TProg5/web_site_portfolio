from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.core.templates import templates, get_translator

router = APIRouter(tags=["Pages"])


@router.route("/")
@router.get("/main", response_class=HTMLResponse, tags=["Pages"])
async def main_page(request: Request):
    lang = request.state.lang
    translator = get_translator(lang=lang)
    
    _ = translator.gettext

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "_": _
        }
    )
