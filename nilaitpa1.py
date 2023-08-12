import streamlit as st

st.title ('Hitung Nilai TPA')

# Masukkan nilai-nilai verbal, numerikal, dan figural
nilai_verbal = st.number_input ("Masukkan Nilai Verbal", 0)
nilai_numerikal = st.number_input ("Masukkan Nilai Numerikal", 0)
nilai_figural = st.number_input ("Masukkan Nilai Figural", 0)

Hitung = st.button('Hitung Nilai TPA')

if Hitung :
    rata_rata = (nilai_verbal + nilai_numerikal + nilai_figural) / 3
    nilai_tpa = ((rata_rata / 100)*600)+200

    st.markdown(f'<p style="font-size: 24px;">Nilai TPA Anda Adalah= {round(nilai_tpa, 2)}</p>', unsafe_allow_html=True)

