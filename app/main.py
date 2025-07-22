import uvicorn

from typing import Any

from fastapi import FastAPI
from app.api import contact
from app.views import pages

from fastapi.staticfiles import StaticFiles


def create_app() -> FastAPI:
    app = FastAPI()

    app.mount(
        path="/static", 
        app=StaticFiles(directory="static"), 
        name="static"
    )
    
    app.include_router(router=contact.router, prefix="/api")
    app.include_router(router=pages.router)
        
    return app

app = create_app()


if __name__ == "__main__":
    uvicorn.run(app="app.main:app", reload=True)
