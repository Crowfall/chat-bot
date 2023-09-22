import streamlit as st
from functions import *

#@st._cache_resource
def load_models():
    return TextProcessor()

text_generator = load_models()

st.title("Hello World")



title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)

st.title("Trad")
st.write(text_generator.openai_text_generativ)