import streamlit as st
import random

# Judul aplikasi
st.title("Simulasi Prediksi Kejadian Petir 1 Jam ke depan⚡")

# Input dari user
suhu = st.number_input("Suhu Udara (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
kelembaban = st.slider("Kelembaban Relatif (%)", min_value=0, max_value=100, value=50)
tekanan = st.number_input("Tekanan QFE (hPa)", min_value=900.0, max_value=1100.0, value=1013.0, step=0.1)
kecepatan_angin = st.number_input("Kecepatan Angin (m/s)", min_value=0.0, max_value=150.0, value=10.0, step=0.1)

# Tombol prediksi
if st.button("Prediksi Kejadian Petir"):
    prediksi = random.choice([0, 1])  # Model dummy: 0 = Tidak Ada Petir, 1 = Ada Petir

    if prediksi == 1:
        st.success("⚡ Prediksi: Petir Mungkin Terjadi!")
    else:
        st.error("🌤 Prediksi: Tidak Ada Petir.")

# Informasi tambahan
st.markdown("**Catatan:** Ini hanyalah simulasi. Model yang sebenarnya memerlukan data historis untuk melatih model prediksi yang lebih akurat.")
