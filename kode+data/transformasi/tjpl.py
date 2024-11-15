# Import library panda untuk proses .csv
import pandas as pd

# Tahap 1 : Load dataset
df = pd.read_csv('D:ML/testp1.csv') # File path dataset

# Tahap 2 : Hitung median dari grup nilai yang digabungkan. axis = 1 digunakan agar hitungan horizontal
df['Spontanitas'] = df[['IBB1', 'IBB2', 'IBB3', 'IBB4']].median(axis=1)
df['Pengaruh Sosial'] = df[['SI1', 'SI2', 'SI3', 'SI4', 'SI5', 'SI6']].median(axis=1)
df['Kesenangan'] = df[['H1', 'H2', 'H3', 'H4']].median(axis=1)
df['Rasionalitas'] = df[['NE1', 'NE2', 'NE3', 'NE4', 'NE5']].median(axis=1)

# Tahap 3 : Buat dataset baru sesuai dengan nilai yang sudah ditransformasi
new_df = df[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Rasionalitas']]

# Tahap 4 : Verifikasi data
print(new_df.head())

# Tahap 5 : Save hasil ke .csv baru
new_df.to_csv('D:ML/tranjpl1.csv', index=False)
print("Proses berhasil : 'D:ML/tranjpl1.csv'")