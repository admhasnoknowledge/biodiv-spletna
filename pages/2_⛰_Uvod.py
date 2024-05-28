import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Triglavski Narodni Park", page_icon=":🏔:",)

st.title("Triglavski Narodni Park")

st.markdown("**Triglavski narodni park** (TNP) se nahaja v središču Julijskih Alp. Imenovan je po _Triglavu_, naši najvišji gori (2864m). Obsega 840km^2, kar je približno 4% površine Slovenije.") 
st.image("img/triglavski_1.jpg")

st.markdown("TNP je znan po svojih razgledih, reliefu in bogati biodiverziteti, ki je tudi zelo vidna. Park je vključen tudi v program **Natura 2000**.")
st.markdown("V parku se opazi veliko raznolikosti zaradi mešanja podnebnih vplivov med Alpami in Sredozemljem, bogat je z različnimi vodnimi telesi in ima zelo razgiban relief.")
st.image("img/triglavski3.jpg", caption="dolina triglavskih jezer")
st.markdown("##### Že samo v tem majhnem delu Slovenije se nahajajo ekosistemi:")
st.markdown("### gozdov, šotnih barij, tekočih vod, visokogorskih jezer, travnikov, melišč in skalnih sten.")
st.markdown("Zemljevid Triglavskega Narodnega Parka")
components.iframe("https://arcg.is/19uuvn2", width=1000, height=800, )
