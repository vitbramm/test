import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import openai
import os

# Укажите свой API-ключ OpenAI
openai.api_key = 'your_openai_api_key'

# Настройки для доступа к Google Drive API
SERVICE_ACCOUNT_FILE = 'path_to_your_service_account_file.json'

# Создаем объект учетных данных
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/drive']
)

# Создаем клиент Google Drive
drive_service = build('drive', 'v3', credentials=credentials)

def extract_text_from_google_drive(file_id):
    # Запрос на получение файла
    file = drive_service.files().get(fileId=file_id).execute()
    file_name = file['name']
    file_content = drive_service.files().get_media(fileId=file_id).execute()
    
    # Запись содержимого файла во временный файл
    with open(file_name, 'wb') as temp_file:
        temp_file.write(file_content)
    
    # Чтение содержимого файла
    with open(file_name, 'r') as temp_file:
        text = temp_file.read()
    
    # Удаление временного файла
    os.remove(file_name)
    
    return text

def process_text_with_llm(text):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=text,
        max_tokens=500
    )
    return response.choices[0].text

st.title("Google Drive File Processing with LLM")
st.write("Введите ссылку на файл в Google Drive для обработки:")

url = st.text_input("Ссылка на файл в Google Drive")
if url:
    try:
        # Извлечение идентификатора файла из URL
        file_id = url.split('/')[-2]
        st.write("Идентификатор файла: ", file_id)
        
        # Извлечение и отображение текста из файла
        text = extract_text_from_google_drive(file_id)
        st.write("Исходный текст:", text)
        
        # Обработка текста с помощью LLM
        processed_text = process_text_with_llm(text)
        st.write("Обработанный текст:", processed_text)
        
        # Сохранение обработанного текста в файл
        with open("processed_text.txt", "w") as f:
            f.write(processed_text)
        
        st.download_button(
            label="Скачать обработанный файл",
            data=processed_text,
            file_name="processed_text.txt",
            mime="text/plain"
        )
        
    except Exception as e:
        st.write("Ошибка при обработке файла:", e)
