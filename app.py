import streamlit as st
import cv2
import polars as pl

def process_image(image):
    grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    clahe=cv2.createCLAHE(clipLimit=3.0,tileGridSize=(5,5))
    clahe_img=clahe.apply(grey_img)
    return clahe_img

def app():
    st.title("Medical Image Enhancement")

    # Allow the user to upload an image file
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    # If an image file is uploaded, display it and process it
    if uploaded_file is not None:
        # Read the image file
        image = cv2.imread(uploaded_file.name)
        # Process the image
        processed_image = process_image(image)

        # Display the input and output images
        st.image(image, caption="Input Image", use_column_width=True)
        st.image(processed_image, caption="Output Image after applying CLAHE", use_column_width=True)

if __name__ == '__main__':
    app()

