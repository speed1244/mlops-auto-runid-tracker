# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from .model import model

app = FastAPI(title="mlflow-demo API")

class IrisInput(BaseModel):
    features: list[float]

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/predict")
def predict(payload: IrisInput):
    # expects 4 float features for iris sample
    arr = [payload.features]
    pred = model.predict(arr)
    return {"prediction": int(pred[0])}
