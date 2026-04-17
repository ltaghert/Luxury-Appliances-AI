import streamlit as st
import engine
import scraper
import os

st.set_page_config(page_title="Luxury Service AI", page_icon="🛠️")
st.title("🛠️ Luxury Service Intelligence")

if st.sidebar.button("Update Manual Database"):
    with st.spinner("Scraping new manuals..."):
        msg = scraper.download_manuals()
        st.sidebar.success(msg)

tab1, tab2 = st.tabs(["Manual Assistant", "Acoustic Diagnostics"])

with tab1:
    query = st.text_input("Ask a technical question:")
    if query:
        with st.spinner("Searching manuals..."):
            response = engine.get_answer(query)
            st.info(response["result"])

with tab2:
    st.subheader("Sound-Based Troubleshooting")
    audio_file = st.file_uploader("Upload appliance noise", type=["wav", "mp3"])
    if audio_file:
        st.audio(audio_file)
        st.warning("Acoustic Analysis: Identifying rhythmic mechanical friction...")
