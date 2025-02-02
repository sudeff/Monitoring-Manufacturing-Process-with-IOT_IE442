import pandas as pd  

# CSV dosyasını yükle
df = pd.read_csv("c8.csv")  

# İlk 5 satırı görüntüle
print(df.head())  

# Veri hakkında genel bilgi al
print(df.info())  

# Eksik verileri kontrol et
print(df.isnull().sum())  


import matplotlib.pyplot as plt  

import datetime

# 2024-01-01 00:00:00 başlangıç kabul edelim
start_time = datetime.datetime(2024, 1, 1)

# Her Timestamp değerini bu başlangıç zamanına ekleyelim
df["timestamp"] = pd.to_datetime(df["Timestamp"].apply(lambda x: start_time + pd.to_timedelta(x, unit="s")))

# Yeni Timestamp sütununu kontrol edelim
print(df[["Timestamp", "timestamp"]].head())

import matplotlib.pyplot as plt

plt.plot(df['timestamp'], df['B_4'], label="B_4 Sensor Data")
plt.xlabel("Time")
plt.ylabel("B_4 Sensor Value")
plt.title("B_4 Sensor Data Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Timestamp sütununu datetime formatına çevir
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Timestamp'ı index yapalım (Zaman serisi analizi için)
df.set_index("timestamp", inplace=True)

# Eksik veri noktalarını önceki en yakın değerle dolduralım
df = df.resample("1S").ffill()  # 1 saniyelik eksik verileri önceki değerle doldur

from scipy.stats import zscore

# Anomalileri tespit etmek için Z-score hesaplayalım
df["B_4_zscore"] = zscore(df["B_4"])  # L_1 sensör verisi için

# Anormal verileri belirleyelim (Z-score |1.8|'den büyükse anomali kabul edilir)
df["anomaly"] = df["B_4_zscore"].apply(lambda x: "Yes" if abs(x) > 1.8 else "No")

# Anormal olmayan verileri seçelim
df_filtered = df[df["anomaly"] == "No"]

# Anomalileri temizlenmiş yeni bir veri seti ile çalışalım
df_filtered.drop(columns=["B_4_zscore", "anomaly"], inplace=True)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df_filtered.index, df_filtered["B_4"], label="B_4 Sensor Data", color="blue")

ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # 1 saatlik aralıklarla göster
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

plt.xlabel("Time")
plt.ylabel("B_4 Sensor Value")
plt.title("B_4 Sensor Data Over Time (Cleaned)")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

df_filtered["B_4_smoothed"] = df_filtered["B_4"].rolling(window=5, center=True).mean()
df_filtered = df_filtered.resample("1S").ffill()  # 1 saniyelik eksik verileri doldur

# Smoothed veriyi görselleştirelim
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df_filtered.index, df_filtered["B_4_smoothed"], label="Smoothed B_4 Sensor Data", color="red")

ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))  
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

plt.xlabel("Time")
plt.ylabel("B_4 Sensor Value (Smoothed)")
plt.title("B_4 Sensor Data Over Time (Smoothed)")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show() 

from statsmodels.tsa.arima.model import ARIMA

# ARIMA modelini eğitmek için zaman serisini seçelim
train_data = df_filtered["B_4_smoothed"].dropna()  # NaN olan satırları çıkaralım

# ARIMA modelini oluştur ve eğit
model = ARIMA(train_data, order=(5, 1, 0))
model_fit = model.fit()

# Gelecek 60 zaman birimi (saniye, dakika, vb.) için tahmin yapalım
forecast = model_fit.forecast(steps=60)

# Tahminleri görselleştirelim
plt.figure(figsize=(12, 6))
plt.plot(train_data.index, train_data, label="Actual Data")
plt.plot(pd.date_range(start=train_data.index[-1], periods=60, freq="S"), forecast, label="Forecast", linestyle="dashed", color="red")
plt.xlabel("Time")
plt.ylabel("B_4 Sensor Value")
plt.title("B_4 Sensor Data Forecasting")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Gerekli kütüphaneleri tekrar yükleyelim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Veri çerçevesini oluştur (Örnek veri seti)
np.random.seed(42)  # Sonuçların tekrarlanabilir olması için

# Örnek veri sayısı
num_samples = 1000

# Sensör verilerini rastgele oluştur (Gerçek veriye benzer)
df = pd.DataFrame({
    "L_1": np.random.uniform(30, 80, num_samples),  # Örnek L_1 verisi (Yük verisi gibi)
    "B_1": np.random.uniform(10, 50, num_samples),  # Örnek B_1 verisi (Titreşim verisi gibi)
})

# Sıcaklık verisini rastgele ekle (Gerçekçi bir dağılım kullanarak)
df["Temperature"] = df["L_1"] * 0.2 + df["B_1"] * 0.1 + np.random.normal(loc=50, scale=3, size=num_samples)

# Veriyi görselleştir
plt.figure(figsize=(10, 5))
plt.plot(df["Temperature"], label="Temperature", color="red", alpha=0.7)
plt.xlabel("Sample Index")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Data Over Time")
plt.legend()
plt.grid()
plt.show()

# Veri çerçevesini görselleştir
import ace_tools as tools
tools.display_dataframe_to_user(name="Temperature Data", dataframe=df)
