from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def preprocess_logs(file_path):
    log_df = pd.read_csv(file_path)
    log_df['timestamp'] = pd.to_datetime(log_df['timestamp'])

    scaler = MinMaxScaler()
    features = ['cpu_usage', 'memory_usage', 'network_traffic']
    log_df[features] = scaler.fit_transform(log_df[features])
    print("preprocessing fin!")
    return log_df

if __name__ == "__main__":
    log_df = preprocess_logs("./data/simulated_logs.csv")
    print(log_df.head(3))