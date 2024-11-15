# Import library panda untuk proses .csv
import pandas as pd

# Tahap 1 : Load dataset
df1 = pd.read_csv('D:ML/tranjpl1.csv')
df2 = pd.read_csv('D:ML/tranjma2.csv')

# Tahap 2 : Dataset digabungkan dengan fungsi concat
combined_df = pd.concat([df1, df2], ignore_index=True)

# Optional: Menghilangkan duplikat data
# combined_df.drop_duplicates(inplace=True)

# Tahap 3 : Verifikasi data
print(combined_df.head())

# Tahap 4 : Save hasil ke .csv baru
combined_df.to_csv('D:ML/cbndf1.csv', index=False)
print("Proses berhasil : 'D:ML/cbndf1.csv'")