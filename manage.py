import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from application.initializer import IncludeAPIRouter
from application.main.config import settings


def get_application():
    _app = FastAPI(
        title=settings.API_NAME,
        description=settings.API_DESCRIPTION,
        version=settings.API_VERSION,
    )

    # Mount the "static" directory to serve static files (e.g., styles.css)
    _app.mount("/static", StaticFiles(directory="static"), name="static")

    _app.include_router(IncludeAPIRouter())
    _app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_origins=["*"],
    )

    return _app


app = get_application()


@app.on_event("shutdown")
async def app_shutdown():
    # on app shutdown do something probably close some connections or trigger some event
    print("On App Shutdown i will be called.")


# uvicorn.run("manage:app", host=settings.HOST, port=settings.PORT, log_level=settings.LOG_LEVEL, use_colors=True,reload=True)
# uvicorn "manage:app" "--host" "0.0.0.0" "--port" "8000" --reload
