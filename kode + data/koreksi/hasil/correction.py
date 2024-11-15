# Import library panda untuk proses .csv
import pandas as pd

# Tahap 1 : Load dataset
df = pd.read_csv('D:ML/clsdf1.csv') # File path dataset

# Tahap 2 : Pembalikan nilai value
df['Irasionalitas'] = 6 - df['Rasionalitas']

# Tahap 3 : Buat dataset baru sesuai dengan nilai yang sudah ditransformasi
new_df = df[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas']]

# Tahap 4 : Verifikasi data
print(new_df.head())

# Tahap 5 : Save hasil ke .csv baru
new_df.to_csv('D:ML/revdata1.csv', index=False)
print("Proses berhasil : 'D:ML/revdata1.csv'")
