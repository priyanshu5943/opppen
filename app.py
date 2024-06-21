import streamlit as st
import cv2
import numpy as np

st.title('OpenCV with Streamlit')

try:
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    image = cv2.circle(image, (50, 50), 40, (255, 0, 0), -1)
    st.image(image, channels="BGR")
    st.write("OpenCV is working correctly.")
except Exception as e:
    st.write(f"An error occurred: {e}")
