import streamlit as st
from functions import TextProcessor
import tempfile
import os

text_processor = TextProcessor()

st.header("Transcription Audio")

audio_file = st.file_uploader("Télécharger un fichier audio (MP3, WAV, etc.)", type=["mp3", "wav"])

if audio_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        temp_audio_file.write(audio_file.read())

    audio_file_path = temp_audio_file.name

    st.success("Fichier audio téléchargé avec succès!")

    if st.button("Démarrer la transcription"):
        text_transcription = text_processor.openai_transcribe(audio_file_path)

        st.header("Voci la transcription du fichier")
        st.write(text_transcription)
        
    os.remove(audio_file_path)