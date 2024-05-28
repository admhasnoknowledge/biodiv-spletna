import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vodni krog v TNP", page_icon="🌊:",)
st.title("Vode v TNP")
st.markdown("Na tej strani se nahaja mala galerija različnih vodnih teles v Triglavskem narodnem parku:")
st.page_link("https://www.tnp.si/sl/park/narava/vodni-krog/", label="Za več: Vodni krog v TNP", icon="🚿")
st.image("img/foto_arhiv_tnp_az_1634.jpg")
st.image("img/foto_arhiv_tnp_az_1708.jpg")
st.image("img/foto_arhiv_tnp_az_1846.jpg")
st.image("img/pokrajina_tnp_134.jpg")