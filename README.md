# Deploy - Linear Regression Model Deployment

## 프로젝트 개요
이 프로젝트는 **Streamlit을 사용한 머신러닝 모델 배포 애플리케이션**입니다.
간단한 선형 회귀(Linear Regression) 모델을 학습하고, 이를 웹 애플리케이션을 통해 배포할 수 있도록 구성되었습니다.

## 주요 기능
- **선형 회귀 모델 학습 (`train_model.py`)**
  - 간단한 데이터셋을 이용해 선형 회귀 모델을 학습
  - 모델을 `model.pkl` 파일로 저장

- **Streamlit 웹 애플리케이션 (`app.py`)**
  - 학습된 모델을 로드하여 사용자 입력값에 대한 예측 수행
  - 사용자 친화적인 UI 제공

- **Docker를 이용한 배포 (`Dockerfile`)**
  - 컨테이너 환경에서 실행 가능

## 프로젝트 구조
```
Deploy/
│── app.py  # Streamlit 웹 애플리케이션 실행 파일
│── train_model.py  # 머신러닝 모델 학습 스크립트
│── model.pkl  # 학습된 머신러닝 모델 (Pickle 형식)
│── requirements.txt  # 필요 라이브러리 목록
│── Dockerfile  # Docker 배포 설정
│── README.md  # 프로젝트 설명 파일
```

## 설치 및 실행 방법
### 1. 필수 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 2. 머신러닝 모델 학습
```bash
python train_model.py
```

### 3. Streamlit 애플리케이션 실행
```bash
streamlit run app.py
```

## Docker 배포 방법
### 1. Docker 이미지 빌드
```bash
docker build -t deploy-app .
```

### 2. 컨테이너 실행
```bash
docker run -p 8501:8501 deploy-app
```

## 필요 라이브러리
- `streamlit`
- `numpy`
- `scikit-learn`
- `pickle`

## 기여 방법
1. 본 레포지토리를 포크합니다.
2. 새로운 브랜치를 생성합니다.
3. 변경 사항을 커밋하고 푸시합니다.
4. Pull Request를 생성하여 기여합니다.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

