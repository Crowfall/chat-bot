import streamlit as st
from functions import TextProcessor

text_processor = TextProcessor()

st.title("Amélioration du texte avec ChatGPT")

user_text = st.text_area("Entrez le texte à améliorer :")

if st.button("Améliorer le texte"):
    if user_text:
        prompt_better = text_processor.generate_prompt_with_chatgpt(user_text)
        st.write("Prompt amélioré :", prompt_better)
    else:
        st.warning("Entrer un texte avant de l'améliorer.")