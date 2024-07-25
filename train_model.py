import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# 간단한 데이터셋 생성
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

# 모델 훈련
model = LinearRegression()
model.fit(X, y)

# 모델 저장
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
