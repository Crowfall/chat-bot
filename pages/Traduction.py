from functions import TextProcessor
import streamlit as st

text_processor = TextProcessor()

# Zone de texte
message = st.text_input(" Que souhaitez-vous traduire ?")

# Bouton Valider
valider = st.button("Valider")

if valider:
    # Connexion à l'API OpenAI
    response = text_processor.openai_translate(message)

    # Choix de la langue
    #langues = list(response.keys())
    #key_langue = st.selectbox("Choix de la langue", langues)
    
    # Affichage de la traduction
    st.write("Traduction : ", response)




