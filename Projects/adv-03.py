#  Face  Recognization using  OpenCV  and  Python

import cv2
import streamlit as st
import time

st.title("Face Recognition using OpenCV and Streamlit")

# Initialize the face detector
face_dec = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize session state
if "running" not in st.session_state:
    st.session_state["running"] = False

# Streamlit buttons
start = st.button("Start Face Recognition")
stop = st.button("Stop Face Recognition")
frame_placeholder = st.empty()

if start:
    st.session_state["running"] = True

if stop:
    st.session_state["running"] = False

video_cap = cv2.VideoCapture(0)
video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while st.session_state["running"]:
    ret, video_data = video_cap.read()
    if not ret:
        st.write("Error: Could not access webcam")
        break

    video_data = cv2.flip(video_data, 1)
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    faces = face_dec.detectMultiScale(
        col, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    frame_placeholder.image(video_data, channels="BGR", use_column_width=True)
    time.sleep(0.05)

video_cap.release()
cv2.destroyAllWindows()
 