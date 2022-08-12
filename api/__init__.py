from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .v1 import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    @app.get("/", include_in_schema=False)
    async def redirect() -> RedirectResponse:
        response = RedirectResponse(url="/docs")
        return response

    return app
