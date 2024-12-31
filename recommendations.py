import streamlit as st

def recommendations_page():
    st.header("Rekomendasi Nutrisi dan Aktivitas untuk Kehamilan")
    
    trimester = st.selectbox(
        "Pilih trimester kehamilan:",
        ["Trimester 1", "Trimester 2", "Trimester 3"]
    )

    if trimester == "Trimester 1":
        st.write("""
        *Rekomendasi Trimester 1:*
        - Konsumsi asam folat untuk perkembangan otak dan sumsum tulang belakang bayi.
        - Hindari stres dan aktivitas berat.
        - Tidur yang cukup.
        """)
    elif trimester == "Trimester 2":
        st.write("""
        *Rekomendasi Trimester 2:*
        - Konsumsi protein, kalsium, dan zat besi untuk mendukung pertumbuhan janin.
        - Mulai olahraga ringan seperti jalan kaki atau yoga.
        """)
    elif trimester == "Trimester 3":
        st.write("""
        *Rekomendasi Trimester 3:*
        - Perbanyak zat besi untuk mencegah anemia.
        - Istirahat yang cukup.
        - Senam kehamilan untuk persiapan persalinan.
        """)
