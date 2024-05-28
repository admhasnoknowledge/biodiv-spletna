import streamlit as st
st.set_page_config(page_title="Triglavski Narodni Park", page_icon=":🍃:", layout="wide")

st.title("Triglavski Narodni Park")
st.markdown("### To je moja naloga za Biologijo v 9. razredu, če imaš kot bralec kakršenkoli predlog, komentar, mi ga pošlji na e-pošto. Če pa ne, pa upam da uživaš v branju! Za začetek ti priporočam uvod." )
st.page_link("pages/2_⛰_uvod.py", label="uvod", icon="🧧")

st.sidebar.success("Izberi stran, ki si jo želiš prebrati")

st.markdown("Avtor: **Adam Grapkić Peternelj**")
st.markdown("mail: adam.grapkic@gmail.com")
st.markdown("viri:")
st.link_button("Spletna stran TNP", "https://www.tnp.si/sl/")
st.link_button("Spletna stran naravni parki Slovenije", "https://www.naravniparkislovenije.si/slo/naravni-parki/triglavski-narodni-park")
