# mlops-auto-runid-tracker

# mlflow-demo (MVP)

Minimal demo:
- Train a simple sklearn model (Iris) and log to MLflow
- Save model to `./model/model.pkl`
- Serve with FastAPI at `/predict`

## Quickstart (local)

1. Create venv & install:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Train model:
```bash
python train.py

3. Run API:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

4. Test:
```bash
# ping
curl http://127.0.0.1:8000/ping

# predict (example features)
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" \
  -d '{"features":[5.1,3.5,1.4,0.2]}'

5. MLflow UI
mlflow ui
