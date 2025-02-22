from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from src.funcitons.inferance import inference

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/predict/")
async def predict(image: UploadFile = File(...)):  # Dosya yüklemesi için UploadFile kullanıyoruz
    try:
        print("Data geldi")
        image_data = await image.read()
        prediction = inference(image_data)
        return JSONResponse(content={"prediction": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
