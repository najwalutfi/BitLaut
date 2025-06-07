import pandas as pd
import matplotlib.pyplot as plt
import os

# Contoh data dummy (bisa diganti dengan data asli)
data = {
    'Tahun': [2018, 2019, 2020, 2021, 2022],
    'Jumlah Kapal': [100, 120, 150, 170, 210],
    'Hasil Tangkapan': [500, 480, 460, 400, 350]
}
df = pd.DataFrame(data)

# Buat grafik
plt.figure(figsize=(10, 5))
plt.plot(df['Tahun'], df['Jumlah Kapal'], marker='o', label='Jumlah Kapal')
plt.plot(df['Tahun'], df['Hasil Tangkapan'], marker='s', label='Hasil Tangkapan')
plt.title('Tren Overfishing')
plt.xlabel('Tahun')
plt.ylabel('Jumlah')
plt.legend()
plt.grid(True)

# Pastikan folder static/ ada
os.makedirs('static', exist_ok=True)

# Simpan grafik ke folder static/
output_path = "C:/Users/Lenovo/datamining/produksi_ikan/static/grafik_overfishing.jpg"
plt.savefig(output_path)
plt.close()

print(f"✅ Grafik berhasil disimpan di {output_path}")