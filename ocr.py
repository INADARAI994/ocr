import streamlit as st
from PIL import Image
import easyocr
import numpy as np

# Initialize EasyOCR reader
reader = easyocr.Reader(['ja', 'en'])

def ocr(img):
    result = reader.readtext(np.array(img))
    result_text = [each_result[1] for each_result in result]
    return "\n".join(result_text)

# Streamlit UI components
st.title("OCRアプリ")

# Option to upload an image
uploaded_file = st.file_uploader("画像ファイルを選択してください、または画像をここにドラッグしてください...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    extracted_text = ocr(image)
    st.subheader("OCR結果")
    st.text(extracted_text)
