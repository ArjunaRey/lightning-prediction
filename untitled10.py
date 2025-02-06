import streamlit as st

# Judul aplikasi
st.title("⚡ Simulasi Prediksi Kejadian Petir")

# Menambahkan logo di sidebar dari GitHub
st.sidebar.image("Stmkg-new.png", width=200)

# Input untuk jam UTC kejadian yang ingin diprediksi
st.subheader("🔹 Masukkan Jam Saat Ini (UTC)")

jam_prediksi_utc = st.number_input("Jam (UTC)", min_value=0, max_value=23, value=12, step=1)

# Input untuk data saat ini
st.subheader("🔹 Masukkan Data Saat Ini")

suhu_sekarang = st.number_input("Suhu Sekarang (°C)", min_value=-10.0, max_value=50.0, value=25.0)
kelembaban_sekarang = st.number_input("Kelembaban Sekarang (%)", min_value=0, max_value=100, value=60)
tekanan_sekarang = st.number_input("Tekanan QFE Sekarang (hPa)", min_value=900.0, max_value=1100.0, value=1013.0)
kecepatan_angin_sekarang = st.number_input("Kecepatan Angin Sekarang (m/S)", min_value=0.0, max_value=150.0, value=10.0)

# Input untuk data 1 jam sebelumnya
st.subheader("🔹 Masukkan Data 1 Jam Sebelumnya")

suhu_1jam_lalu = st.number_input("Suhu 1 Jam Lalu (°C)", min_value=-10.0, max_value=50.0, value=24.0)
kelembaban_1jam_lalu = st.number_input("Kelembaban 1 Jam Lalu (%)", min_value=0, max_value=100, value=58)
tekanan_1jam_lalu = st.number_input("Tekanan QFE 1 Jam Lalu (hPa)", min_value=900.0, max_value=1100.0, value=1012.0)
kecepatan_angin_1jam_lalu = st.number_input("Kecepatan Angin 1 Jam Lalu (m/S)", min_value=0.0, max_value=150.0, value=9.0)

# Input untuk data 2 jam sebelumnya
st.subheader("🔹 Masukkan Data 2 Jam Sebelumnya")

suhu_2jam_lalu = st.number_input("Suhu 2 Jam Lalu (°C)", min_value=-10.0, max_value=50.0, value=23.0)
kelembaban_2jam_lalu = st.number_input("Kelembaban 2 Jam Lalu (%)", min_value=0, max_value=100, value=56)
tekanan_2jam_lalu = st.number_input("Tekanan QFE 2 Jam Lalu (hPa)", min_value=900.0, max_value=1100.0, value=1011.0)
kecepatan_angin_2jam_lalu = st.number_input("Kecepatan Angin 2 Jam Lalu (m/S)", min_value=0.0, max_value=150.0, value=8.0)

# Menampilkan data yang dimasukkan oleh user
st.subheader("📊 Data yang Dimasukkan")
st.write("**Data Saat Ini:**")
st.write(f"Suhu: {suhu_sekarang}°C, Kelembaban: {kelembaban_sekarang}%, Tekanan: {tekanan_sekarang} hPa, Kecepatan Angin: {kecepatan_angin_sekarang} m/S")

st.write("**Data 1 Jam Lalu:**")
st.write(f"Suhu: {suhu_1jam_lalu}°C, Kelembaban: {kelembaban_1jam_lalu}%, Tekanan: {tekanan_1jam_lalu} hPa, Kecepatan Angin: {kecepatan_angin_1jam_lalu} m/S")

st.write("**Data 2 Jam Lalu:**")
st.write(f"Suhu: {suhu_2jam_lalu}°C, Kelembaban: {kelembaban_2jam_lalu}%, Tekanan: {tekanan_2jam_lalu} hPa, Kecepatan Angin: {kecepatan_angin_2jam_lalu} m/S")


# Jika tombol prediksi ditekan, lakukan prediksi sederhana (misalnya menggunakan model dummy)
if st.button("Prediksi Kejadian Petir 1 Jam ke depan"):
    # Contoh prediksi dummy: jika suhu saat ini lebih tinggi dan kelembaban lebih tinggi, maka petir lebih mungkin
    if suhu_sekarang > suhu_2jam_lalu and kelembaban_sekarang > kelembaban_2jam_lalu:
        st.success("⚡ Prediksi: Petir Mungkin Terjadi!")
    else:
        st.error("🌤 Prediksi: Tidak Ada Petir.")
