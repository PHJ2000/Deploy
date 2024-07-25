import streamlit as st
import numpy as np
import pickle

st.title('Linear Regression Model')

# 모델 파일 확인 및 로드
model_path = 'model.pkl'
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    st.success('Model loaded successfully.')
except FileNotFoundError:
    st.error(f'Model file {model_path} not found. Please ensure model.pkl is in the correct location.')
except Exception as e:
    st.error(f'An error occurred while loading the model: {e}')

# 입력 값 받아서 예측 수행
input_value = st.number_input('Input value:', value=0)

if st.button('Predict'):
    try:
        prediction = model.predict(np.array([[input_value]]))
        st.write(f'Prediction: {prediction[0]}')
    except NameError:
        st.error('Model is not loaded. Please check the model file.')
    except Exception as e:
        st.error(f'An error occurred during prediction: {e}')
