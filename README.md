# mlops-auto-runid-tracker

Minimal demo:
- Model Training: Trains a simple Iris model and logs the process with MLflow.

- Model Saving: The trained model is saved as a .pkl file for deployment.

- API Service: A FastAPI server provides a /predict endpoint for the model.

- MLflow UI: The MLflow interface helps you visualize and manage all experiment runs.

## Quickstart

1. Build the Training Image
```bash
docker build -t [docker_image_name] -f Dockerfile.train .
```

2. Run the Training Container
```bash
docker run --rm -v $(pwd)/model:/app/model [docker_image_name]
```

3. Build docker image and run the API server:
```bash
docker build -t [docker_image_name] -f Dockerfile.fastapi .
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

## To-Do List
1. ~~Containerize Training (train.py): Create a Dockerfile to package the training script for a reproducible environment.~~

3. Enhance API Health Check: Add a /health endpoint to verify if the model is loaded correctly.

5. Parameterize Training Script: Use argparse to allow command-line parameters for training runs.

7. Add API Unit Tests: Write pytest unit tests for the /predict endpoint to ensure reliability.

9. Implement API Versioning: Add versioning (e.g., /v1/predict) to the API endpoints.

11. Deploy with Kubernetes: Use Kubernetes to deploy and manage the FastAPI service for scalability and high availability.