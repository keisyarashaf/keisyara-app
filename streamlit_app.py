import streamlit as st

st.title("choi san gf :3")
st.write(
    "༓ 𓂃  “a garden bloomed in her defiance.” kissed by fairy, anointed in moonlight. 🪽 [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("e18c3d400063873ec1c8bba9bb46a206.jpg")
st.write("\n")

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap atau Ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"(angka) adalah bilangan genap")
else:
  st.write(f"(angka) adalah bilangan ganjil")
