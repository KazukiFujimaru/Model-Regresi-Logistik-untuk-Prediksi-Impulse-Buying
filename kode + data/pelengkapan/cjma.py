# Import library panda untuk proses .csv, numpy untuk matematika
import pandas as pd
import numpy as np

# Tahap 1 : Load dataset
df = pd.read_csv('D:ML/Raw_Data_Jurnal_Mobile_App.csv')  # File path dataset

# Tahap 2 : Cek data
totalds = len(df)
print(f'Total data: {totalds}')

# Tahap 3 : Set ratio gender
ratio_gender = [259/628, 369/628]  # Laki-laki : 41.24%, Perempuan : 58.76%
ratio_umur = [154/628, 386/628, 88/628]  # Ratio umur : 24.5%, 61.5%, 14%

# Tahap 4 : Penambahan variabel secara acak
df['Gender'] = np.random.choice(['0', '1'], size=totalds, p=ratio_gender) # 0 Laki-laki, 1 Perempuan
df['Age Group'] = np.random.choice(['1', '2', '3'], size=totalds, p=ratio_umur) # ratio'26-30', '31-35', '36-40'

# Tahap 5: Verifikasi data
print(df['Gender'].value_counts(normalize=True))  # Cek ulang ratio gender
print(df['Age Group'].value_counts(normalize=True))  # Cek ulang ratio umur

# Tahap 6 : Testing data
print(df.head())

# Tahap 7 : Save hasil ke .csv baru
df.to_csv('D:ML/testj3.csv', index=False)
print("Proses berhasil : D:ML/testj3.csv")