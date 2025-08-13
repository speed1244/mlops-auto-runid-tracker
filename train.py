# train.py
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path

# config
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("iris-demo")
MODEL_DIR = Path("model")
MODEL_DIR.mkdir(parents=True, exist_ok=True)
MODEL_FILE = MODEL_DIR / "model.pkl"

# load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# eval
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

# --- FIX: Get a sample input for the model signature ---
# Take the first row of the test data as an example input.
input_example = X_test[:1]

# mlflow log + save model to local file
with mlflow.start_run() as run:
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_metric("accuracy", float(acc))
    mlflow.sklearn.log_model(model, name="model", input_example=input_example)
    # also save a simple pickle for API to load easily
    joblib.dump(model, MODEL_FILE)

print(f"✅ Trained. accuracy={acc:.4f}")
print(f"✅ Model saved to {MODEL_FILE}")
print("ℹ️ MLflow runs stored under ./mlruns/")

