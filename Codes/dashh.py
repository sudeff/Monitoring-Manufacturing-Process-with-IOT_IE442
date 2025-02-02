import streamlit as st
import pandas as pd
import plotly.express as px

# Sayfa başlığı
st.set_page_config(page_title="IoT Manufacturing Dashboard", layout="wide")

st.title("📊 IoT Manufacturing Data Dashboard")
st.write("Bu dashboard, üretim sürecindeki sensör verilerini görselleştirmek için oluşturulmuştur.")

# Veri yükleme fonksiyonu
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\SUDE\Desktop\442 research project\C8.csv")

  # Eğer CSV ise: pd.read_csv("C8.csv")

df = load_data()

# Sidebar (Yan Menü)
st.sidebar.header("⚙️ Ayarlar")
sensor_choice = st.sidebar.selectbox("📡 Sensör Seç:", df.columns[1:])
refresh_button = st.sidebar.button("🔄 Veriyi Güncelle")

# Zaman bazlı grafik
fig = px.line(df, x=df.columns[0], y=sensor_choice, title=f"{sensor_choice} Sensör Verisi")
st.plotly_chart(fig, use_container_width=True)

# Histogram (Veri Dağılımı)
fig_hist = px.histogram(df, x=sensor_choice, title=f"{sensor_choice} Değer Dağılımı")
st.plotly_chart(fig_hist, use_container_width=True)

# Verinin son 10 satırını göster
st.subheader("📌 Son 10 Veri Noktası")
st.write(df.tail(10))

# Canlı veri güncelleme
if refresh_button:
    st.experimental_rerun()


import streamlit as st
import pdfkit
import os

st.title("📊 IoT Manufacturing Data Dashboard")
st.write("Bu dashboard, üretim sürecindeki sensör verilerini görselleştirmek için oluşturulmuştur.")

# Buton ile dashboard'un HTML çıktısını PDF'ye çevirme
if st.button("📄 PDF Olarak İndir"):
    pdfkit.from_url("http://localhost:8501", "dashboard.pdf")  # Eğer lokal çalışıyorsa
    st.success("PDF başarıyla oluşturuldu! Dosya adı: dashboard.pdf")

