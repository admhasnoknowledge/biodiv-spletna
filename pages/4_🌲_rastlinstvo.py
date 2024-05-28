import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Rastlinstvo v TNP", page_icon=":🌲:",)

st.title(":green[Rastline v TNP]")

st.markdown("V Triglavskem narodnem parku je tudi veliko rastlin in velik delež njih je tudi zaščiten. Poglej si nekaj znanih primerov spodaj:")

st.title("Planika")
st.markdown("Planika (Leontopodium alpinum) je trajnica, visoka do 20 cm. Njen cvet ima od 5 do 6 majhnih rumenih cvetov, od koder tudi ime očnica. Rumeni cvetovi so obkroženi z belkastimi listi.")
st.image("img/planika_2.jpg", caption="Planika je prva zavarovana rastlina v Sloveniji.")

st.title("Zoisova zvončnica")
st.markdown("Zoisova zvončica (Campanula zoysii) je ena izmed najprepoznavnejših rastlin našega visokogorja. Je edina med zvončicami, ki ima stisnjeno ustje cvetnega venca. Raste v apnenčastih skalnatih razpokah. Spada med endemite, kar pomeni, da uspeva na omejenem geografskem območju jugovzhodnih Alp.")
st.markdown("### Ustje cvetov je pri Zoisovi zvončici tako ozko, da žuželke skozenj ne morejo priti. Za opraševanje morajo napraviti luknjo v cvetu.")
st.image("img/zoisova_zvoncica_1.jpg", caption="Ime je dobila po Karlu Zoisu, slovenskem botaniku, ki jo je odkril; preučil, opisal in poimenoval pa jo je znan botanik Franz Xaver von Wulfen.")

st.title("Triglavski dimek")
st.markdown("Triglavski dimek (Crepis terglouensis) je nizkorastoča trajnica, ki nekoliko spominja na regrat. Spada v družino radičevk. Cvet je sestavljen iz stotih majhnih jezičastih cvetov, ki so združeni v socvetje. Plod je suh in opremljen z dlačicami. Vsa rastlina vsebuje grenak mleček.")
st.image("img/triglavski_dimek(c960x540).jpg", caption="V Triglavskem narodnem parku je najbolj razširjen na južnih pobočjih Triglava nad Velim poljem.")

st.link_button("Klikni me za več!", "https://www.tnp.si/sl/park/narava/rastlinstvo/")