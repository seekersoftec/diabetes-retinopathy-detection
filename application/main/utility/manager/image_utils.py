import os
import pandas as pd
from io import BytesIO
from PIL import Image
from application.main.config import settings


class BasicImageUtils:
    @classmethod
    async def read_image_file(cls, file, filename, cache=True) -> (Image.Image, str, pd.DataFrame):
        image = Image.open(BytesIO(file))
        file_path = ""
        if cache:
            file_path: str = os.path.join(settings.APP_CONFIG.CACHE_DIR, filename)
            image.save(file_path)

        dataframe = pd.DataFrame({
                        'Images': [0],
	                    'image_name': [filename]
                    })
        return image, file_path, dataframe
