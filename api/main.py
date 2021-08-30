from fastapi import FastAPI , File , UploadFile 
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
# from starlette.routing import Host
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
app = FastAPI()

MODEL = tf.keras.models.load_model("../1")
Class_Names = ["Early Blight" , "Late Blight" , "Healthy"]

@app.get("/")
async def home():
    return "home screen"


@app.get("/ping")
async def ping():
    return "hello world"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict( 
    file:UploadFile  = File(...)
    ):
    # return "hello world"
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image,0)
    predictions = MODEL.predict(img_batch)
    pass


if __name__ == "__main__":
    uvicorn.run(app)
