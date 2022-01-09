import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()

st.title("Language Detection Tool")
input_test = st.text_input("Provide your text here","e.g. Hello there! My name is Farhana.")
button_clicked = st.button("Get language name!")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))