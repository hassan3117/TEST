import streamlit as st

st.title("Streamlit on Google Colab!")
st.write("This is a Streamlit app running in Google Colab with ngrok.")

# Add more Streamlit components if needed
name = st.text_input("Enter your name:")
st.write("Hello, ", name)