# Use a lightweight Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy and install all Python packages
# Allow Docker to cache the results of pip install.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application and trained model
COPY app/ ./app/
COPY model/ ./model/

# Expose the port used by the application
EXPOSE 8000

# Start FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

