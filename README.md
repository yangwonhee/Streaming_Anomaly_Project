# 🛠️ Streaming_Anomaly_Project

머신러닝 모델을 이용한 실시간 이상 탐지 slack 알림 서비스.
2024.12.03 현재 진행 중인 프로젝트입니다. 

---

## 📋 **Project Overview**

✅ 본 프로젝트의 목표
"__Docker로 컨테이너화된 FastAPI를 사용해 모델을 서빙하고, 입력 데이터에 따른 예측 결과를 Slack으로 실시간 알림__"

- FastAPI, Docker, Slack webhook의 경험을 할 수 있음.
- 모델은 간단한 isolation forest 사용.

---

## 📂 **Repository Structure**

📦 Isolation-Forest-Anomaly-Detection 
```
project/
├── data/
│   └── simulated_logs.csv          # 로그 데이터 파일
│   ├── isolation_forest_model.pkl  # trained model
├── src/
│   ├── data_generator.py           # 로그 데이터 random 생성 코드
│   ├── preprocess.py               # 데이터 전처리 코드 (MinMaxScaler)
│   ├── train_model.py              # 모델 학습 코드 (Isolation Forest)
│   ├── serve_api.py                # FastAPI 기반 API 코드
│   └── streaming.py                # 실시간 로그 스트리밍 코드 (Slack)
├── requirements.txt                # 프로젝트에 필요한 라이브러리 목록
└── README.md                       # 프로젝트 설명 문서
```

---

## 🚀 **Getting Started**

**1. Clone the Repository**
```bash
git clone https://github.com/your-username/Isolation-Forest-Anomaly-Detection.git
cd Isolation-Forest-Anomaly-Detection
```

**2. Install Dependencies**

```bash
pip install -r requirements.txt
```

**3. Create the Dataset**
```bash
python src/data_generator.py 
```

**4. Preproccessing**
```bash
python src/preprocess.py
```

**5. Training Model**
```bash
python src/train_model.py
```

**6. Running FastAPI**
```bash
python src/serve_api.py
```

**7. Streaming and Send message to Slack**
파일 실행 전, '.env' 파일 생성 후 ```SLACK_WEBHOOK_URL```을 입력해놓기.

```bash
python src/streaming.py
```