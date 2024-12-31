import streamlit as st

def gejala_kesehatan_page():
    st.title("🩺 Gejala Kesehatan Kehamilan")
    st.markdown(
        """
        **Selamat datang!**
        
        Di sini, Anda bisa memeriksa **gejala-gejala** yang umum terjadi selama kehamilan dan memahami kapan Anda harus berkonsultasi dengan dokter.
        Pilih gejala di bawah untuk mendapatkan penjelasan lebih lanjut. 😊
        """
    )

    # Daftar gejala kehamilan
    gejala = {
        "🤢 Mual dan muntah": "Mual dan muntah adalah gejala yang umum terutama pada trimester pertama.\nJika berlangsung lama atau menyebabkan dehidrasi, segera konsultasikan dengan dokter.",
        "🦴 Nyeri punggung": "Nyeri punggung sering terjadi karena perubahan postur tubuh.\nJika disertai dengan pembengkakan atau nyeri parah, konsultasikan dengan dokter.",
        "🤕 Sakit kepala": "Sakit kepala bisa disebabkan oleh perubahan hormon atau stres.\nJika disertai dengan penglihatan kabur atau pembengkakan tangan dan kaki, segera periksa ke dokter.",
        "🦶 Pembengkakan kaki": "Pembengkakan kaki biasa terjadi, tetapi jika disertai dengan nyeri atau pendarahan, ini bisa menjadi tanda masalah.\nHubungi dokter jika pembengkakan terjadi secara tiba-tiba atau tidak normal.",
        "😕 Perubahan suasana hati": "Perubahan suasana hati adalah gejala biasa karena perubahan hormon.\nJika disertai dengan depresi berat, segera temui konselor atau dokter.",
        "🤰 Kram perut": "Kram perut bisa normal, terutama pada trimester pertama. Namun, jika disertai pendarahan, segera periksakan ke dokter.",
        "😮\u200d💨 Sesak napas": "Sesak napas dapat terjadi karena perubahan hormonal, tetapi jika terjadi terus-menerus atau parah, segera konsultasikan ke dokter.",
        "❤️ Sakit di dada": "Sakit di dada tidak boleh dianggap enteng. Jika disertai dengan sesak napas, segera ke rumah sakit.",
        "🩸 Pendarahan atau flek": "Pendarahan atau flek bisa terjadi, tetapi bisa juga tanda masalah serius seperti keguguran atau kehamilan ektopik.\nHubungi dokter segera jika mengalami pendarahan.",
        "✋ Mati rasa atau kesemutan": "Mati rasa atau kesemutan pada tangan/kaki bisa terjadi akibat perubahan sirkulasi darah. Namun, jika berlanjut atau parah, konsultasikan dengan dokter."
    }

    # Menampilkan pilihan gejala
    selected_gejala = st.radio("Pilih gejala yang Anda alami:", list(gejala.keys()))
    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown(f"### {selected_gejala.split()[0]}")
        st.write(":point_left: **Info Gejala**")

    with col2:
        st.markdown(f"""
        ### Penjelasan
        {gejala[selected_gejala]}
        """)

    # Footer dengan saran tambahan
    st.markdown(
        """
        ---
        ⚠️ **Catatan Penting:**
        Jika Anda merasa khawatir dengan kondisi Anda, jangan ragu untuk segera menghubungi tenaga medis profesional.
        """
    )

if __name__ == "__main__":
    gejala_kesehatan_page()
