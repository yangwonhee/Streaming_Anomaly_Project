import pandas as pd 
import numpy as np
from datetime import datetime, timedelta

def generate_logs(num_records, file_path):
    timestamps = [datetime.now() - timedelta(minutes=i) for i in range(num_records)]
    cpu_usage = np.random.normal(50, 10, num_records).clip(0, 100)
    memory_usage = np.random.normal(70, 15, num_records).clip(0, 100)
    network_traffic = np.random.normal(200, 50, num_records).clip(0, 500)
    anomalies = [1 if np.random.rand() < 0.05 else 0 for _ in range(num_records)]
    
    log_df =  pd.DataFrame({
        "timestamp": timestamps,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "network_traffic": network_traffic,
        "anomaly": anomalies  
    })

    log_df.to_csv(file_path, index = False)
    print("== log data saved as: {} ==" .format(file_path))

if __name__ == "__main__":
    generate_logs(1000, "./data/simulated_logs.csv")