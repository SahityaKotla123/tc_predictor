from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json
import numpy as np

app = FastAPI()

model = joblib.load("tc_model.pkl")
features = json.load(open("features.json"))

class InputData(BaseModel):
    press_GPa: float
    ave_valency: float
    valency_per_H: float
    r_ion_Angstrom: float

@app.get("/")
def home():
    return {"message": "Superconductor Tc Predictor is running"}

@app.post("/predict")
def predict(data: InputData):
    values = [[data.press_GPa, data.ave_valency, data.valency_per_H, data.r_ion_Angstrom]]
    prediction = model.predict(values)
    return {"predicted_Tc_K": round(float(prediction[0]), 2)}