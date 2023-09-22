import streamlit as st
from functions import *


st.title("Entrainement GT3.5 turbo")

up = st.file_uploader("choisir fichier")

try:
    path_file = "temp/data.jsonl"
    bytes_data = up.read()
    with open(path_file) as f:f.write(bytes_data)

except:
    pass

if st.button("start training"):
    try:
        id_model = TextProcessor().openai_chat_finetune(path_file)
        st.write(f"le modele : {id_model}")
    except:
        st.error("fichier non chargé")