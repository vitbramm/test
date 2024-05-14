import streamlit as st
import pandas as pd
import numpy as np

st.title('Мое первое Streamlit приложение лялялялляля')

st.write("Вот таблица данных:")
data = pd.DataFrame({
    'Переменная A': np.random.randn(10),
    'Переменная B': np.random.randn(10)
})
st.write(data)

if st.button('Показать график'):
    st.line_chart(data)
