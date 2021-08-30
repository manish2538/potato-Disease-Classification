from fastapi import FastAPI , File , UploadFile 
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
# from starlette.routing import Host
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return "home screen"


@app.get("/ping")
async def ping():
    return "hello world"


@app.post("/predict")
async def predict( 
    file:UploadFile  = File(...)
    ):
    # return "hello world"
    image = await file.read()
    pass


if __name__ == "__main__":
    uvicorn.run(app)
