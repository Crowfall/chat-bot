from functions import *
import streamlit as st

# Zone de texte
message = st.text_input(" Que souhaitez-vous generer ?")

# Bouton Valider
valider = st.button("Valider")

if valider:
    # Connexion à l'API OpenAI
    response = TextProcessor().openai_text_generativ(message)

    # Choix de la langue
    #langues = list(response.keys())
    
    #key_langue = st.selectbox("Choix de la langue", langues)
    
    # Affichage de la traduction
    st.write("generativ : ", response)




