from functions import *
import streamlit as st

# Zone de texte
message = st.text_area(" Que souhaitez-vous corriger ?")

# Bouton Valider
valider = st.button("Valider")

if valider:
    # Connexion à l'API OpenAI
    response = TextProcessor().openai_codex(message)

    # Choix de la langue
    #langues = list(response.keys())
    
    #key_langue = st.selectbox("Choix de la langue", langues)
    
    # Affichage de la traduction
    st.write("Correction : ", response)




