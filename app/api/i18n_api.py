from fastapi import APIRouter, Response

from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.response import APIResponse

router = APIRouter(tags=["i18n"])


@router.post("/locale/{lang}", description="Changes the user's language in cookies", tags=["i18n"])
async def get_user_locale(lang: str, response: Response):
    if lang not in settings.SUPPORTED_LOCALE:
        return JSONResponse(
            content=APIResponse(
                success=False, 
                message=f"Unsupported language"
            ).model_dump()
        )
    
    response = JSONResponse(
        content=APIResponse(
            success=True, 
            message=f"Set new {lang} language at the cookies"
        ).model_dump()
    )

    response.set_cookie(
        key="lang", 
        value=lang,
        max_age=60*60*24*365,
        path="/",
        samesite="lax"
    )

    return response