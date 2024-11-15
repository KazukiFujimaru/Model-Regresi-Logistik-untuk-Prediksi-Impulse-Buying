# Import library panda untuk proses .csv
import pandas as pd

# Tahap 1 : Load dataset
df = pd.read_csv('D:/ML/testj3.csv') # File path dataset

# Tahap 2 : Hitung median dari grup nilai yang digabungkan. axis = 1 digunakan agar hitungan horizontal
df['Spontanitas'] = df[['IB1', 'IB2', 'IB3']].median(axis=1)
df['Pengaruh Sosial'] = df[['SE1', 'SE2', 'SE3']].median(axis=1)
df['Kesenangan'] = df[['HB1', 'HB2', 'HB3']].median(axis=1)
df['Rasionalitas'] = df[['UB1', 'UB2', 'UB3', 'UB4', 'UB5']].median(axis=1)

# Tahap 3 : Buat dataset baru sesuai dengan nilai yang sudah ditransformasi
new_df = df[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Rasionalitas']]

# Tahap 4 : Verifikasi data
print(new_df.head())

# Tahap 5 : Save hasil ke .csv baru
new_df.to_csv('D:ML/tranjma2.csv', index=False)
print("Proses berhasil : 'D:ML/tranjma2.csv'")