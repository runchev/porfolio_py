import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

info = """
Hi i am Boro Runchev, designer with 10 years experience.

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

with col1:
    st.image("images/photo.png")
with col2:
    st.info(info)
