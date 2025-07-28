import uvicorn
from typing import Any

from fastapi import FastAPI

from app.api import contact, i18n_api
from app.views import pages

from app.middlewares.i18n_middleware import i18nMiddleware

from fastapi.staticfiles import StaticFiles


def create_app() -> FastAPI:
    app = FastAPI()

    app.mount(
        path="/static", 
        app=StaticFiles(directory="static"), 
        name="static"
    )
    
    app.include_router(router=contact.router, prefix="/api")
    app.include_router(router=i18n_api.router, prefix="/api")
    app.include_router(router=pages.router)

    app.add_middleware(i18nMiddleware(app=app))

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app="app.main:app", reload=True)
