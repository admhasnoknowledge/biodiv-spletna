import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Živali v TNP", page_icon=":🐐:",)

if st.button("🏠"):
    st.switch_page("TriglavskiNarodniPark.py")
if st.button("➡"):
    st.switch_page("pages/4_🌲_Rastlinstvo.py")
if st.button("⬅"):
    st.switch_page("pages/2_⛰_Uvod.py")

st.title(":red[Živali v TNP]")

st.markdown("V Triglavskem narodnem parku naj bi po sedanjih podatkih živelo okoli :rainbow[7.000] različnih vrst. Spodaj so predstavljeni znani (in meni zanimivi) predstvniki:")

st.title("Alpski Kozorog")
st.markdown("Alpski kozorog (Capra ibex) je močna, čokata koza s sivkasto dlako. Živi na gorskih traviščih nad gozdno mejo, v zimskem času pa se spusti tudi do gozdne meje. V skalnem svetu je izredno spreten. Z mesta lahko skoči 2 m visoko, z zaletom do 4 m.")
st.image("img/alpski_kozorog_4.jpg", caption="Alpski kozorog se uspešno pari z domačo kozo.")

st.title("Gams")
st.markdown("Gams (Rupicapra rupicapra) je najznačilnejša žival alpskega sveta. V poletnih mesecih se zadržuje v odprtih skalnatih predelih nad gozdno mejo, pozimi pa tudi v gozdovih. V hudih zimah pride čisto do dolin. Poleti so gamsi aktivni zjutraj in zvečer, pozimi pa so njihove aktivnosti porazdeljene čez ves dan.")
st.image("img/gams_2.jpg", caption="Gamsi so družabna bitja, živijo v skupinah.")

st.title("Alpski Svizec")
st.markdown("Alpski svizec (Marmota marmota) je bil v času ledenih dob na območju današnje Slovenije splošno razširjen in pogost, ob koncu ledene dobe pa je izumrl. V prejšnjem stoletju je bil ponovno naseljen. Danes živi na gorskih travnikih in meliščih.")
st.image("img/alpski_svizec_1.jpg", caption="Temperatura Alpskega svizca Je med zimskim spancem enaka zunanji. V primeru, da gre temperatura pod ledišče, se zbudijo.")

st.title("Soška Postrv")
st.markdown("Soška postrv (Salmo marmoratus) je sladkovodna ribja vrsta, ki živi samo v Jadranskem povodju. V Sloveniji naseljuje Sočo s pritoki, Reko in Rižano.")
st.image("img/soska_postrv_foto_michel_roggo.jpg", caption="Največja Soška postrv je merila 121 cm in tehtala 25 kg.")

st.text("Za več si poglej:")
st.link_button("Živalstvo v TNP", "https://www.tnp.si/sl/park/narava/zivalstvo/")