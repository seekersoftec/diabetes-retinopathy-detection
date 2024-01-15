import pandas as pd
from application.main.config import settings
from application.initializer import LoggerInstance
from application.main.infrastructure.classification.image.inference_dr import (
    InferenceTask,
)


class ImageClassificationService(object):
    def __init__(self):
        self.logger = LoggerInstance().get_logger(__name__)
        self.image_model = InferenceTask()
        self.image_classification_model = "desnet"  # settings.MOBILENET_V2
        self.IMAGE_SHAPE = (320, 320)  # (224, 224)

    async def classify(self, image_file, file_path: str, dataframe: pd.DataFrame):
        self.logger.info(f"Model IN use : {self.image_classification_model}")
        prediction = await self.image_model.predict(
            classifier_model_name=self.image_classification_model,
            image=image_file,
            file_path=file_path,
            dataframe=dataframe,
        )
        return prediction
