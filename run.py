import streamlit as st


# Configuration de la page
st.set_page_config(
    page_title="Streamlit OpenAI APP",
    page_icon="🧊",
    layout="wide",
)

# Ttitle
st.title("Streamlit OpenAI APP")

# Sous-titre
st.subheader("Utilisation des modèles de GPT-3")

# Texte Markdown
st.markdown(
    """
    Cette application est un exemple d'utilisation de l'API OpenAI pour générer du texte.

    `pip install openai`

    - Gpt-3
    - Gpt-4
    """
)

data_user = {
    'name' : 'Kevin',
    'age' : 30,
    'job' : 'Data Scientist',
    'ville' : 'Paris'
}

# Checkbox
if st.checkbox("Afficher les données"):
    st.write(data_user)

# Formulaire
with st.form(key='my_form'):
    nom = st.text_input("Quel est votre nom ?")

    submit_button = st.form_submit_button(label='Envoyer')

    if submit_button :
        st.write("Votre nom est : ", nom)


# Création de colonnes
col1, col2 = st.columns(2)

with col1:
    st.title("Colonne 1")
    st.selectbox("Choix", ["A", "B", "C"])
    st.button("Valider")
    
    

with col2:
    st.title("Colonne 2")
    st.date_input("Date")
    st.select_slider("Age", range(1, 100))


# Bare latérale
st.sidebar.title("Sidebar")
st.sidebar.button("Valider 1", key='1')