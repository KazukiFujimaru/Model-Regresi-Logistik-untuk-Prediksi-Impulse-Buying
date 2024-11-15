# Import library panda untuk proses .csv
import pandas as pd

# Tahap 1 : Load dataset
df = pd.read_csv('D:/ML/Raw_Data_PayLat.csv')  # File path dataset

# Tahap 2 : Patokan Bins umur 
bin_umur = [18, 25, 30, 35, 40, 45, 50, 55, 60]  # Patokan atas pengelompokkan
label_umur = [0, 1, 2, 3, 4, 5, 6, 7]  # Label untuk tiap grup

# Tahap 3 : Penggunaan pd.cut untuk kategorasasi umur ke grup umur
df['Age Group'] = pd.cut(df['Age'], bins=bin_umur, labels=label_umur, right=True)

# Tahap 4 : Verifikasi data
print(df[['Age', 'Age Group']].head())

# Tahap 5 : Save hasil ke .csv baru
df.to_csv('D:ML/testp1.csv', index=False)
print("Proses berhasil : 'D:ML/testp1.csv'")
