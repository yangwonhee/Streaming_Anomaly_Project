import json
import numpy as np
import time
import requests
import os
from dotenv import load_dotenv

# producer = KafkaProducer(
#     bootstrap_servers="localhost:9092",
#     value_serializer=lambda v:json.dumps(v).encode("utf-8")
# )

load_dotenv()  
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
API_URL = "http://localhost:8000/predict"

def send_slack_message(webhook_url, message):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Successed to send Slack message")
    else:
        print("Failed to send slack message: {}, {}" .format(response.status_code, response.text))


# 실시간 로그 생성과 전송
while True:
    log = {
        "cpu_usage": np.random.uniform(20, 90),
        "memory_usage": np.random.uniform(30, 95),
        "network_traffic": np.random.uniform(100,500)
    }
    print("sending log: {}".format(log))
    # producer.send("log_topic", log)

    # if log['cpu_usage'] > 85:
    #     send_slack_message(SLACK_WEBHOOK_URL, "CPU 사용량 초과 경고: {}%" .format(log['cpu_usage']))
    
    response = requests.post(API_URL, json=log)
    if response.status_code == 200:
        prediction = response.json()
        print(f"예측 결과: {prediction}")
        if prediction['anomaly_predicted'] == 1:
            send_slack_message(SLACK_WEBHOOK_URL, "이상탐지경고: {}".format(log))
    else:
        print("API 요청 실패: {}, {}".format(response.status_code, response.text))
    time.sleep(1)