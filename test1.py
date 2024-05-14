import streamlit as st

# Функция для имитации обработки текста
def process_text(text):
    # Здесь будет ваш алгоритм обработки текста
    processed_text = text.upper()  # Например, преобразуем текст в верхний регистр
    return processed_text

st.title("Приложение для обработки текста")

st.write("Введите текст для обработки:")

# Поле для ввода текста
text_input = st.text_area("Текст для обработки")

if st.button('Обработать'):
    if text_input:
        # Обрабатываем текст
        processed_text = process_text(text_input)
        st.write("Обработанный текст:")
        st.write(processed_text)

        # Кнопка для скачивания обработанного текста
        st.download_button(
            label="Скачать обработанный текст",
            data=processed_text,
            file_name="processed_text.txt",
            mime="text/plain"
        )
    else:
        st.write("Пожалуйста, введите текст для обработки.")
