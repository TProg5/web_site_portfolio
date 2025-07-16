from fastapi import FastAPI
from app.api import contact
from app.views import pages

from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.mount(
    path="/static", 
    app=StaticFiles(directory="static"), 
    name="static"
)

app.include_router(
    router=contact.router,
    prefix="/api"
)

app.include_router(
    router=pages.router
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)