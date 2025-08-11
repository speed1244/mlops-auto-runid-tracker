# app/model.py
from pathlib import Path
import joblib
import os

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "model" / "model.pkl"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Please run `python train.py` first.")

# load model once at import time (fastapi import)
model = joblib.load(MODEL_PATH)

