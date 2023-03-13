import functions as ft
import streamlit as st

ft.topluHaberEkle()
gunluk_trends=ft.trendsfull()
df=ft.haberGetir()

st.sidebar.title("Anlık Keyword")
gunluk_trends.reverse()
for a in gunluk_trends:
    st.sidebar.error(a[0])


dakika=round(df['kalan'].dt.total_seconds()/60)
sozluk = dict(zip(df['Başlık'],dakika))

col1,col2=st.columns([3,1])
with col1:
    st.subheader("Başlık")
with col2:
    st.subheader("Kalan Süre")

for haber in sozluk.keys():
    col1,col2=st.columns([3,1])
    with col1:

        st.write(haber)
    with col2:

        st.write(sozluk[haber],"dk")
    st.markdown("""---""")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .viewerBadge_container__1QSob {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
