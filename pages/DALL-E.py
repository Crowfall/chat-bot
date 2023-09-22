import streamlit as st
from functions import *


if st.checkbox('Création d\'image avec OpenAI'):
    prompt = st.text_input('Quel sujet vous intéresse ?')
    valider = st.button('Valider')

    if valider:
        img_url = TextGenerator().openai_image_creation(prompt)

        TextGenerator().doanload_image(img_url, 'img.png')
        st.image('img.png', width=500)


if st.checkbox('Création d\'une variante avec OpenAI'):
    try:
        uploaded_file = st.file_uploader("Choose a CSV file")
        bytes_data = uploaded_file.read()
    except:
        pass

    try:
        url_img = TextGenerator().openai_image_variant(bytes_data)
        TextGenerator().doanload_image(url_img, './variation.png')
        st.image('variation.png', width=500)
    except:
        pass