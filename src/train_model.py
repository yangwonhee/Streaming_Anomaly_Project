from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib

def train_model(data_path, model_path):
    # isolation forest model training
    log_df = pd.read_csv(data_path)
    X = log_df[['cpu_usage', 'memory_usage', 'network_traffic']]
    model = IsolationForest(n_estimators= 100, contamination=0.05, random_state=42)
    model.fit(X)

    joblib.dump(model, model_path)
    print("training fin! {}" .format(model_path))

if __name__ == "__main__":
    train_model("./data/simulated_logs.csv", "./data/isolation_forest_model.pkl")

# log_df['anomaly_score'] = model.decision_function(X)
# log_df['anomaly_predicted'] = model.predict(X) # -1이면 이상값

# print(log_df[['timestamp', 'cpu_usage', 'anomaly_score', 'anomaly_predicted']].head(3))
