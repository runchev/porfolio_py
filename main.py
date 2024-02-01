import streamlit as st
import functions

title_row = functions.get_row_from_csv(rowname="title", separator=";")
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

col3, col4 = st.columns(2)
with col3:
    for item in title_row[:10]:
        st.write("<h3>" + item + "</h3>", unsafe_allow_html=True)
with col4:
    for item in title_row[10:]:
        st.write("<h3>" + item + "</h3>", unsafe_allow_html=True)
