import pandas as pd

# Tahap 1 : Load dataset
df = pd.read_csv('D:ML/revdata1.csv') # File path dataset

# Step 1: Hitung Composite Score (Sebelumnya Rationalitas)
df['Composite Score'] = df[['Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas']].mean(axis=1)

# Step 2: Define the Threshold
threshold = 2.7

# Step 3: Assign Impulse Buying Labels
df['Impulse Buying'] = (df['Composite Score'] > threshold).astype(int)
new_df = df[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas', 'Impulse Buying']]

# Display the updated df with labels
print(df)

# Tahap 4 : Verifikasi data
print(new_df.head())

new_df.to_csv('D:ML/datahasil4.csv', index=False)
print("Proses berhasil : 'D:ML/datahasil4.csv'")
