from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import Settings, settings

class i18nMiddleware(BaseHTTPMiddleware):
    """
    Middleware that intercepts new users without the language set in the cookies.\n
    Will otherwise pass the language to the next endpoint being called.

    :param: 
    **app**: `FastAPI()` - An instance of the `FastAPi` application

    """
    def __init__(
        self, 
        app, 
        dispatch = None, 
        settings: Settings = settings
    ) -> None:
        super().__init__(app, dispatch)
        self.settings = settings

    async def dispatch(self, request: Request, call_next):
        lang = request.cookies.get("lang")

        if lang not in self.settings.SUPPORTED_LOCALE:
            lang = self.settings.DEFAULT_LOCALE

        request.state.lang = lang
        response = await call_next(request)

        if request.cookies.get("lang") != lang:
            response.set_cookie(
                key="lang", 
                value=lang,
                max_age=60*60*24*365,
                path="/",
                samesite="lax"
            )

        return response