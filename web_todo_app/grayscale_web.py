import streamlit as sl
from PIL import Image

with sl.expander("start camera"):
    # start camera
    cam = sl.camera_input("camera")


uploaded = sl.file_uploader("upload image")

if cam:
    # create a pillow image instance
    image = Image.open(cam)

    # L is the argument to convert to grayscale
    gray = image.convert("L")

    # render the grayscale image on the webpage
    sl.image(gray)

if uploaded:
    # create a pillow image instance
    image = Image.open(uploaded)

    # L is the argument to convert to grayscale
    gray = image.convert("L")

    # render the grayscale image on the webpage
    sl.image(gray)

