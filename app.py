import streamlit as st
from trimester import trimester_page
from bmi_calculator import bmi_calculator_page
from recommendations import recommendations_page
from gejala_kesehatan import gejala_kesehatan_page  # Import halaman baru Gejala Kesehatan

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Dashboard Kehamilan",
    page_icon="🤰",
    layout="wide"
)

# Sidebar untuk navigasi
st.sidebar.title("")
menu = st.sidebar.radio(
    "Pilih Fitur:",
    ["Dashboard", "Pemantauan Trimester", "Kalkulator BMI", "Rekomendasi Nutrisi", "Gejala Kesehatan"]
)

# Dashboard utama
if menu == "Dashboard":
    st.title("Dashboard Pemeriksaan Kehamilan")
    st.markdown("""
    Selamat datang di aplikasi Pemeriksaan Kehamilan. 
    Aplikasi ini dirancang untuk membantu ibu hamil dalam beberapa hal  :
    - Pemantauan trimester kehamilan
    - Menghitung berat badan ideal (BMI)
    - Mendapatkan rekomendasi nutrisi dan aktivitas fisik
    - Memeriksa gejala-gejala kesehatan yang umum
    
    Pilih fitur yang diinginkan melalui menu di sidebar. 😊
    """)
    
elif menu == "Pemantauan Trimester":
    trimester_page()

elif menu == "Kalkulator BMI":
    bmi_calculator_page()

elif menu == "Rekomendasi Nutrisi":
    recommendations_page()

elif menu == "Gejala Kesehatan":
    gejala_kesehatan_page()
    
    import streamlit as st

# Custom CSS untuk tampilan
st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
        background-color: #fffff;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #48D1CC;
        color: white;
        padding: 5px;
    }
    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 16px;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    [data-testid="stSidebar"] *:hover {
        color: #ecf0f1 !important;
    }
    /* Header bar styling */
    header[data-testid="stHeader"] {
        background-color:#AFEEEE;
        color: white;
        padding: 5px;
        
    }
    header[data-testid="stHeader"] h1 {
        color: white;
        font-size: 10px;
    }
    .stButton > button:hover {
        background-color: #2980b9;
        color: #ecf0f1;
    }
    /* Custom title style for Kas Masjid */
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 20px;
        text-align: center;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)