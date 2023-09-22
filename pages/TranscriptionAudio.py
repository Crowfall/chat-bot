import streamlit as st
from functions import TextProcessor
from audio_recorder_streamlit import audio_recorder


text_processor = TextProcessor()

st.title("Transcription audio en temps réel")

audio_bytes = audio_recorder()

if audio_bytes:
    with open("temp_audio.wav", "wb") as audio_file:
        audio_file.write(audio_bytes)

    transcribed_text = text_processor.openai_transcribe("temp_audio.wav")

    st.audio(audio_bytes, format="audio/wav")
    st.write("Transcription audio en temps réel :")
    st.write(transcribed_text)
