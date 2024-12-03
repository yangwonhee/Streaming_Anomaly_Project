from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import numpy as np


model = joblib.load("./data/isolation_forest_model.pkl")
app = FastAPI()

model_features = ['cpu_usage', 'memory_usage', 'network_traffic']

class LogData(BaseModel):
    cpu_usage: float
    memory_usage: float
    network_traffic: float

@app.post("/predict")
def predict_anomaly(log: LogData):
    # data = np.array([log.cpu_usage, log.memory_usage, log.network_traffic])
    # anomaly_score = model.decision_function(data)[0]
    # anomaly_predicted = model.predict(data)[0]

    data = np.array([[log.cpu_usage, log.memory_usage, log.network_traffic]])  # 차원 조정
    anomaly_score = model.decision_function(data)[0]
    anomaly_predicted = model.predict(data)[0]
    return {
        "anomaly_score": anomaly_score,
        "anomaly_predicted": int(anomaly_predicted == -1)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)