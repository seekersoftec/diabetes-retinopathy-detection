from tensorflow.keras.preprocessing.image import ImageDataGenerator
from application.initializer import LoggerInstance
from application.main.config import settings
from PIL import Image
import numpy as np
import cv2
import tensorflow as tf
import pandas as pd

# import aiofiles
# import os

# from aiofiles import FileNotFoundError, PermissionError


# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
logger = LoggerInstance().get_logger(__name__)
classifier_model = None

# Model parameters
HEIGHT = 320
WIDTH = 320
IMG_SIZE = 320
sigmaX = 10


# async def clear_directory(directory_path):
#     """Clears all files and subdirectories within the specified directory."""
#     try:
#         async with aiofiles.open(
#             os.path.join(directory_path, ".keep"), "w"
#         ) as f:  # Create an empty ".keep" file to prevent directory removal
#             pass

#         async for entry in aiofiles.os.scandir(directory_path):
#             if entry.is_file():
#                 await aiofiles.os.remove(entry.path)
#             elif entry.is_dir():
#                 await clear_directory(entry.path)  # Recursively clear subdirectories

#         # If you want to remove the directory itself as well:
#         # await aiofiles.os.rmdir(directory_path)

#     except FileNotFoundError:
#         print(f"Directory '{directory_path}' not found.")
#     except PermissionError:
#         print(f"Insufficient permissions to clear directory '{directory_path}'.")
#     except Exception as e:
#         print(f"An error occurred while clearing the directory: {e}")


def load_ben_color(image):
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image = cv2.addWeighted(image, 4, cv2.GaussianBlur(image, (0, 0), sigmaX), -4, 128)
    # Convert to grayscale
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image


def img_generator(dataframe: pd.DataFrame, directory=settings.APP_CONFIG.CACHE_DIR):
    data_gen = ImageDataGenerator(
        rescale=1 / 255.0,
        zoom_range=0.2,  # 0.15
        fill_mode="constant",
        cval=0.0,
        horizontal_flip=True,
        brightness_range=[0.8, 1.2],  # Randomize brightness
        preprocessing_function=load_ben_color,
    )

    new_generator = data_gen.flow_from_dataframe(
        dataframe=dataframe,
        directory=directory,
        x_col="image_name",
        batch_size=1,
        class_mode=None,
        target_size=(HEIGHT, WIDTH),
        shuffle=False,
    )

    return new_generator


class InferenceTask:
    @staticmethod
    async def load_model(classifier_model_name):
        if classifier_model_name == "MOBILENET_V2":
            model = tf.keras.applications.MobileNetV2(weights="imagenet")
        elif classifier_model_name == "INCEPTION_V3":
            model = tf.keras.applications.InceptionV3(weights="imagenet")
        else:
            model = tf.keras.models.load_model(
                settings.APP_CONFIG.DR_CLASSIFICATION_MODEL
            )  # tf.keras.applications.MobileNetV2(weights="imagenet")

        return model

    @staticmethod
    async def decode_predictions(predictions):
        class_labels = {1: "Referable", 0: "Non_Referable"}

        _class = [np.argmax(pred) for pred in predictions]
        _confidence = predictions[0]

        return {
            "label": int(_class[0]),
            "class": class_labels[int(_class[0])],
            "confidence": f"{_confidence[1] * 100:0.2f}%",
        }

    async def predict(
        self,
        classifier_model_name: str,
        image: Image.Image,
        file_path: str,
        dataframe: pd.DataFrame,
    ):
        global classifier_model
        if classifier_model is None:
            classifier_model = await self.load_model(classifier_model_name)

        new_generator = img_generator(dataframe)
        label_step_size = new_generator.n // new_generator.batch_size
        label_preds = classifier_model.predict(
            new_generator, steps=label_step_size, verbose=1
        )

        result = await self.decode_predictions(label_preds)
        # logger.info(f"Result => {result}")

        # await clear_directory(file_path)

        return result
