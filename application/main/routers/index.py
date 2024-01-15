from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from application.initializer import LoggerInstance

router = APIRouter()
logger = LoggerInstance().get_logger(__name__)


templates = Jinja2Templates(
    directory="templates"
)  # Assuming the HTML file is in the "templates" directory


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @router.get("/")
# async def hello_world():
#     logger.info('Hello World👍🏻')
#     return JSONResponse(content={"message": "Hello World! 👍🏻"}, status_code=200)
