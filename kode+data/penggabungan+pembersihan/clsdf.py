# Import library panda untuk proses .csv
import pandas as pd

# Tahap 1 : Load dataset
df = pd.read_csv('D:ML/cbndf1.csv') # File path dataset

# Tahap 2 : Membulatkan nilai koma
df['Spontanitas'] = df['Spontanitas'].round()
df['Pengaruh Sosial'] = df['Pengaruh Sosial'].round()
df['Kesenangan'] = df['Kesenangan'].round()
df['Rasionalitas'] = df['Rasionalitas'].round()

# Tahap 3 : Mengubah data ke Interger
df['Spontanitas'] = df['Spontanitas'].astype(int)
df['Pengaruh Sosial'] = df['Pengaruh Sosial'].astype(int)
df['Kesenangan'] = df['Kesenangan'].astype(int)
df['Rasionalitas'] = df['Rasionalitas'].astype(int)

# Tahap 4 : Verifikasi Data
print(df.head())

# Tahap 5 : Save hasil ke .csv baru
df.to_csv('D:ML/clsdf1.csv', index=False)
print("Proses berhasil : 'D:ML/clsdf1.csv'")