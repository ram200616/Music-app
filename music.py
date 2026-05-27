import streamlit as st
import pandas as pd
import os

FILE_NAME = "music_zanabka.csv"

if not os.path.exists(FILE_NAME):
    db = pd.DataFrame(columns=["user", "Artist", "song"])
    db.to_csv(FILE_NAME, index=False)

st.title("Manaik Music")

with st.form("music_form", clear_on_submit=True):
    user = st.text_input("Name (حط اسمك يا عرص)")
    artist = st.text_input("Artist (اسم المغني الشريف)")
    song = st.text_input("Song (اسم الغناي)")
    submitted = st.form_submit_button("submitted")

    if submitted:
        if user and artist and song:
            new_data = pd.DataFrame({
                "user": [user],
                "Artist": [artist],
                "song": [song],
            })
            new_data.to_csv(FILE_NAME, mode="a", header=False, index=False)
            st.success("it's saved (رائع)")
        else:
            st.error("عبي كل المربعات شرموط، بدي ضل علم بربكن")

st.subheader("previous songs")

db_reader = pd.read_csv(FILE_NAME)

st.dataframe(db_reader, use_container_width=True)
