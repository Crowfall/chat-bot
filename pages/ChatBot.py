import streamlit as st
from functions import TextProcessor
from audio_recorder_streamlit import audio_recorder

text_processor = TextProcessor()

st.title("Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if not st.session_state.messages:
    st.chat_message("assistant").markdown("Bonjour, voici les commandes disponibles :\n"
                                        "- `[Texte]`: Taper n'importe quoi pour le retranscrire en audio.\n"
                                        "- `/image [description]` : Pour afficher une image en fonction de la description.\n"
                                        "- `/record` : Pour enregistrer un message audio et le transcrire.\n"
                                        "- `/generativ [mots clés]` : Pour génerer un texte à partir de mots clés.\n"
                                        "- `/summary [texte]` : Pour créer un resumer à partir d'un texte\n"
                                        "- `/code [code]` : Pour corriger le code.\n"
                                        "- `/translate [mots ou phrase]` : Pour traduire des mots ou une phrase.")


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt == "/record":
        st.write("Démarrez l'enregistrement audio en cliquant sur le bouton ci-dessous.")
        audio_bytes = audio_recorder()
        
        if audio_bytes:
            with open("temp_audio.wav", "wb") as audio_file:
                audio_file.write(audio_bytes)

            transcribed_text = text_processor.openai_transcribe("temp_audio.wav")

            st.audio(audio_bytes, format="audio/wav")
            st.write("Transcription audio :")
            st.write(transcribed_text)

    elif prompt.startswith("/image "):
        image_description = prompt[len("/image "):]

        improved_description = text_processor.generate_prompt_with_chatgpt(image_description)

        st.markdown(f"{improved_description}")

        image_url = text_processor.openai_image_creation(improved_description)

        st.image(image_url, caption=f"{improved_description}", use_column_width=True)

        # if "chien" in improved_description.lower():
        #     image_path = "chien.png"
        # elif "chat" in improved_description.lower():
        #     image_path = "cat.png"
        # elif "corentin" in improved_description.lower():
        #     image_path = "LEGO.png"
        # elif "aimen" in improved_description.lower():
        #     image_path = "choux.png"
        # else:
        #     image_path = "default_image.png"

        # st.image(image_path, caption=f"{improved_description}", use_column_width=True)

    elif prompt.startswith("/generativ"):
        message = prompt[len("/generativ "):]  # Récupérer le texte après la commande
        response = text_processor.openai_text_generativ(message)
        st.write("Texte générer :\n", response)

    elif prompt.startswith("/translate"):
        message = prompt[len("/translate "):]
        response = text_processor.openai_translate(message)
        st.write("Traduction : ", response)

    elif prompt.startswith("/code"):
        message = prompt[len("/code "):]
        response = text_processor.openai_codex(message)
        st.write("Correction : ", response)

    elif prompt.startswith("/summary"):
        message = prompt[len("/summary "):]
        response = text_processor.oepenai_text_sumary(message)
        st.write("Résumer : ", response)

    else:
        response = f"Echo: {prompt}"
        with st.chat_message("assistant"):
            audio_path = text_processor.text_to_speech(prompt, "/temp/audio.mp3")
            st.audio(audio_path, format="audio/wav")
            #st.markdown(audio_path, response)
        st.session_state.messages.append({"role": "assistant", "content": response})


        