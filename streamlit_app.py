import functions as ft
import streamlit as st

ft.topluHaberEkle()
df=ft.haberGetir()


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

