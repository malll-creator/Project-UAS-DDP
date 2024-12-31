import streamlit as st

def bmi_calculator_page():
    st.header("Hitung Berat Badan Ideal")

    # Menyediakan input untuk jumlah orang yang ingin dihitung BMI-nya
    jumlah_orang = st.number_input("Berapa banyak orang yang ingin dihitung BMI-nya?", min_value=1, max_value=10, step=1)
    
    for i in range(jumlah_orang):
        st.subheader(f"Orang {i + 1}")
        
        # Input berat dan tinggi badan untuk setiap orang
        berat = st.number_input(f"Masukkan berat badan orang {i + 1} (kg):", min_value=0.0, step=0.1, key=f"berat_{i}")
        tinggi = st.number_input(f"Masukkan tinggi badan orang {i + 1} (cm):", min_value=0.0, step=0.1, key=f"tinggi_{i}")
        
        # Hitung BMI jika tombol hitung diklik
        if st.button(f"Hitung BMI Orang {i + 1}", key=f"hitung_{i}"):
            if tinggi > 0:
                bmi = berat / ((tinggi / 100) ** 2)
                st.write(f"BMI orang {i + 1} adalah {bmi:.2f}")
                
                # Klasifikasi BMI
                if bmi < 18.5:
                    st.write("Kategori: Kekurangan berat badan")
                elif 18.5 <= bmi < 24.9:
                    st.write("Kategori: Berat badan normal")
                elif 25 <= bmi < 29.9:
                    st.write("Kategori: Kelebihan berat badan")
                else:
                    st.write("Kategori: Obesitas")
            else:
                st.write(f"Tinggi badan orang {i + 1} harus lebih besar dari 0!")
