# mlops-auto-runid-tracker


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
```

2. Train model:
```bash
python train.py
```

3. Build docker image and run the API server:
```bash
docker build -t [docker_image_name] .
docker run -p 8000:8000 [docker_image_name]
```

4. Test APIs:
```bash
# ping
curl http://127.0.0.1:8000/ping
# predict
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"features":[5.1,3.5,1.4,0.2]}'
```

5. Run MLflow UI
```bash
mlflow ui
```

6. Open the following URL to check the MLflow UI
default port is 5000
```bash
http://127.0.0.1:5000/#/experiments
```