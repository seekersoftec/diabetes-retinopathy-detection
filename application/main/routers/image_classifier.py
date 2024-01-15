import base64
from fastapi import File, Request, UploadFile
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from application.initializer import LoggerInstance
from application.main.services.image_classification_service import (
    ImageClassificationService,
)
from application.main.utility.manager.image_utils import BasicImageUtils

image_classification_service = ImageClassificationService()
router = APIRouter(prefix="/image-classify")
logger = LoggerInstance().get_logger(__name__)


@router.post("/")
async def image_classification(file: UploadFile = File(...)):
    try:
        # Check file extension
        extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
        if not extension:
            raise ValueError("Image must be jpg or png format!")

        logger.info("Image Classification")

        # Read image file
        image, file_path, dataframe = await BasicImageUtils.read_image_file(
            await file.read(), filename=file.filename, cache=True
        )

        # Perform image classification
        image_category = await image_classification_service.classify(
            image, file_path, dataframe
        )

        # image_category = {"filename": file.filename, "data": "predict"}

        image_category["filename"] = file.filename
        
        logger.info(f"image_category => {image_category}")

        # Return JSON response with image category
        return JSONResponse(content={"data": image_category}, status_code=200)

    except ValueError as ve:
        # Handle invalid image format
        raise ValueError(str(ve)) from ve
        # return JSONResponse(content={"error": str(ve)}, status_code=400)
