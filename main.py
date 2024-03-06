import langchain_helper as lch
import streamlit as st
import textwrap
from annotated_text import annotated_text


left, mid, right, light = st.columns(4)
with left:
   st.sidebar.image("./image1.gif")

st.sidebar.title(":pushpin: YourTube")
annotated_text(
    ("Made by", "Guryuvraj Singh"),
)

st.sidebar.caption("Welcome to YourTube, the revolutionary platform that transforms how you interact with YouTube videos! YourTube is designed for curious minds and enthusiastic learners who seek more from their video experience." )

st.sidebar.caption("Ask Questions on Any YouTube Video: Ever watched a YouTube video and wished you could ask a question directly on a specific scene or moment? YourTube makes this possible. Select any video, pinpoint the exact moment that intrigues you, and post your question. It's that simple!")


# st.sidebar.caption("Fill the fields to do ")
with st.form("my_form"):
        # writing_type = st.selectbox("What is eassay type?", ("Research Paper", "Essay", "Report", "Article"))
        youtube_url = st.text_area(label="What is the Youtube video URL?", max_chars=50)
        st.caption("For example: https://www.youtube.com/watch?v=gbJzL6IJig0")
        query= st.text_area(label="Ask me about video?", max_chars=50, key="query")
        st.caption("For example: Explain how he got the passes.")
        submitted = st.form_submit_button("Submit")


if submitted:
    if query and youtube_url:
        db = lch.create_vector_db_from_youtube_url(youtube_url)
        response,docs = lch.get_response_from_query(db,query)
        st.subheader("Response: ")
        st.text(textwrap.fill(response, width=80 ))
    


