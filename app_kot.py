import streamlit as st
import pandas as pd
import time
import datetime
import random

date = datetime.date

datetime = time.time
questions = pd.read_csv(
    "questions.csv",
    sep=";",
)
rand = random.randint(0, len(questions) - 1)

st.title(f"Smalltalk-O-Mat")
st.markdown("Deine tägliche Frage(n):\n")
st.markdown(questions["question"].iloc[rand])
random_selection = st.button("Random new")
if random_selection:
    rand = random.randint(0, len(questions) - 1)

edited = st.data_editor(questions, hide_index=True, num_rows="dynamic")
edited.to_csv("questions.csv", index=False, sep=";")
