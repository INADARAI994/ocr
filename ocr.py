import streamlit as st
from PIL import Image, ImageGrab
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
uploaded_file = st.file_uploader("画像ファイルを選択してください...", type=["jpg", "png", "jpeg"])

# Option to paste an image from the clipboard
if st.button("クリップボードから画像をペースト"):
    try:
        image = ImageGrab.grabclipboard()
        if image is not None:
            extracted_text = ocr(image)
            st.subheader("OCR結果")
            st.text(extracted_text)
        else:
            st.write("クリップボードに画像が見つかりません。")
    except Exception as e:
        st.write("クリップボードから画像をペースト中にエラーが発生しました: ", str(e))

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    if st.button("アップロードされた画像でOCRを実行"):
        extracted_text = ocr(image)
        st.subheader("OCR結果")
        st.text(extracted_text)
