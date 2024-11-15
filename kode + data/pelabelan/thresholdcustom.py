# Kode berikut dibantu dengan AI untuk memudahkan proses
# mengidentifikasi dan mengklasifikasikan data berdasarkan kriteria yang telah
# ditentukan.

# Nilai Komposit adalah nilai yang mewakili tingkatan atau peringkat.
# Disini Nilai Komposit adalah rata-rata dari Spontanitas, Pengaruh Sosial, Kesenangan, dan Irasionalitas
# Kode ini digunakan dua kali untuk menghasilkan datahasil6.csv dan datahasil7.csv
# Saat ini, kode yang ditulis disini digunakan untuk menghasilkan datahasil7.csv

import pandas as pd

# Tahap 1 : Load dataset
dataset = pd.read_csv('D:/ML/revdata1.csv') # File path dataset

# Tahap 2 : Membuat treshold kustom
thresholds = {
    (0, 0): 2.7,  # Male, Age Group 0
    (0, 1): 2.8,  # Male, Age Group 1
    (0, 2): 3.0,  # Male, Age Group 2
    (0, 3): 3.1,  # Male, Age Group 3
    (0, 4): 3.2,  # Male, Age Group 4
    (0, 5): 3.3,  # Male, Age Group 5
    (0, 6): 3.4,  # Male, Age Group 6
    (0, 7): 3.5,  # Male, Age Group 7

    (1, 0): 2.6,  # Female, Age Group 0
    (1, 1): 2.7,  # Female, Age Group 1
    (1, 2): 2.9,  # Female, Age Group 2
    (1, 3): 3.0,  # Female, Age Group 3
    (1, 4): 3.1,  # Female, Age Group 4
    (1, 5): 3.2,  # Female, Age Group 5
    (1, 6): 3.3,  # Female, Age Group 6
    (1, 7): 3.4   # Female, Age Group 7
}


# Tahap 3 : Menghitung nilai komposit (nilai peringkat)
def calculate_composite(row):
    return (row['Spontanitas'] + row['Pengaruh Sosial'] + row['Kesenangan'] + row['Irasionalitas']) / 4

# Tahap 4 :  Mengaplikasikan nilai komposit
dataset['Composite_Score'] = dataset.apply(calculate_composite, axis=1)

# Tahap 5 : Membuat fungsi untuk menggunakan treshold kustom
# Default thresholdnya 3.5 (digunakan jika data tidak memiliki gender atau umur)
def get_threshold(row):
    return thresholds.get((row['Gender'], row['Age Group']), 3.5)

# Tahap 6 : Menggunakan treshold kustom untuk setiap data
dataset['Impulse Buying'] = dataset.apply(lambda row: 1 if row['Composite_Score'] > get_threshold(row) else 0, axis=1)

# Tahap 7 : Verifikasi Isi data
print(dataset[['Gender', 'Age Group', 'Composite_Score', 'Impulse Buying']])
count_0 = (dataset['Impulse Buying'] == 0).sum()
count_1 = (dataset['Impulse Buying'] == 1).sum()
print(f"Count of Impulse Buying = 0: {count_0}")
print(f"Count of Impulse Buying = 1: {count_1}")

# Tahap 8 : Mendefinisikan Dataset
new_df = dataset[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas', 'Impulse Buying']]

# Tahap 9 : Save hasil ke .csv baru
new_df.to_csv('D:/ML/datahasil7.csv', index=False)
print("Proses berhasil : 'D:/ML/datahasil7.csv'")