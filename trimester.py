import streamlit as st

class trimester:
    def __init__(self, usia_kehamilan, nama, umur):
        self.usia_kehamilan = usia_kehamilan
        self.nama = nama
        self.umur = umur
        self.trimester = self.tentukan_trimester()

    def tentukan_trimester(self):
        """Menentukan trimester berdasarkan usia kehamilan"""
        if self.usia_kehamilan <= 13:
            return "Trimester 1"
        elif 14 <= self.usia_kehamilan <= 27:
            return "Trimester 2"
        elif 28 <= self.usia_kehamilan <= 40:
            return "Trimester 3"
        else:
            return "Tidak Valid"

    def rekomendasi(self):
        """Mengembalikan rekomendasi berdasarkan trimester"""
        if self.trimester == "Trimester 1":
            return []
        elif self.trimester == "Trimester 2":
            return []
        elif self.trimester == "Trimester 3":
            return []
        else:
            return ["Usia kehamilan tidak valid."]

# Fungsi untuk halaman Streamlit
def trimester_page():
    st.header("Pemantauan Kehamilan")

    # Input Nama dan Umur Pasien
    nama = st.text_input("Masukkan nama Anda:")
    umur = st.number_input("Masukkan umur Anda (tahun):", min_value=1, step=1)

    # Input Usia Kehamilan
    usia_kehamilan = st.number_input("Masukkan usia kehamilan (minggu):", min_value=0, max_value=40, step=1)

    if usia_kehamilan > 0 and nama and umur:
        kehamilan = trimester(usia_kehamilan, nama, umur)
        st.write(f"Nama: {kehamilan.nama}")
        st.write(f"Umur: {kehamilan.umur} tahun")
        st.write(f"Anda berada di *{kehamilan.trimester}*")
        st.write("Informasi Kehamilan Anda:")
        for rekomendasi in kehamilan.rekomendasi():
            st.write(f"- {rekomendasi}")
    else:
        st.error("Pastikan semua data (nama, umur, usia kehamilan) sudah dimasukkan.")
