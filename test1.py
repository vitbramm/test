import os
import streamlit as st
from llama_parse import LlamaParse  # Убедитесь, что вы установили пакет с помощью pip install llama-parse

# Установите ваш API ключ
API_KEY = "your_api_key_here"

# Инициализация парсера
parser = LlamaParse(
    api_key=llx-Qx3GKnjxmVc7hz29umtTuoXgq5TycKppFcfIZJb05c0GY6tk,
    result_type="text"  # Вы можете использовать "markdown" или "text" в зависимости от ваших потребностей
)

# Создаем временную директорию, если она не существует
temp_dir = "./temp/"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Создаем интерфейс для загрузки файла
st.title("Resume Parser with LlamaParse")
uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    # Сохраняем загруженный файл во временную директорию
    temp_file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"Uploaded {uploaded_file.name}")
    
    # Парсинг файла
    documents = parser.load_data(temp_file_path)

    # Преобразуем результат в текстовый формат и сохраняем в файл
    parsed_text = documents[0].content
    parsed_file_path = os.path.join(temp_dir, f"parsed_{uploaded_file.name}.txt")
    with open(parsed_file_path, "w") as f:
        f.write(parsed_text)

    # Отображаем результат и добавляем кнопку для скачивания
    st.text_area("Parsed Resume Content", parsed_text, height=400)
    
    with open(parsed_file_path, "rb") as f:
        st.download_button(
            label="Download Parsed Text",
            data=f,
            file_name=f"parsed_{uploaded_file.name}.txt",
            mime="text/plain"
        )
