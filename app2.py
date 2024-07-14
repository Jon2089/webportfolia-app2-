import streamlit as st
import pandas

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

text = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
My contact info: joni@joker.com  phone number: 0123
I am also a tutor. I teach maths, physics and engineering.
"""
st.write(text)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
