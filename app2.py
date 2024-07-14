import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Abdul Rehman Mohsin")
    content = """
    Assalamualaikum, I am Abdul Rehman. Trying to learn python :).
    Right now, I am working at CureMD
    """
    st.info(content)