import streamlit as st
import pandas

info = """
Hi i am Boro, designer with 10 years experience.

Excellent knowledge in Adobe Creative Suit application
InDesign
Adobe Photoshop
Adobe Illustrator

Creating pre press materials
Leaflet
Books
Publications
Cards
Personalized documents/barcodes

Also, i have some knowledge in programing(Pyton, PHP, .NET), so i may a help you with your projects and application.s

Check my portfolio with some of project that i've created.
Feel free to contact me in any time, about any question that you have.
"""

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.title("Boro Runchev")
    st.info(info)

st.write("<b>Below you can find some of my projects, that i've build in, in my career.</b>", unsafe_allow_html=True)

df = pandas.read_csv("data.csv", sep=";")

col3, emptycol, col4 = st.columns([1.5,0.5,1.5])
with col3:
    for index, item in df[:10].iterrows():
        st.write("<h3>" + item["title"] + "</h3>", unsafe_allow_html=True)
        st.write(item["description"])
        st.image("images/" + item["image"])
        st.link_button("Link", url=item["url"])
with col4:
    for index, item in df[10:].iterrows():
        st.write("<h3>" + item["title"] + "</h3>", unsafe_allow_html=True)
        st.write(item["description"])
        st.image("images/" + item["image"])
        st.link_button("Link", url=item["url"])