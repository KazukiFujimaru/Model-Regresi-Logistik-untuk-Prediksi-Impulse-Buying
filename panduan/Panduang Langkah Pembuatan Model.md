# Langkah lengkap proses Machine Learning

## Persiapan Data
- Menyiapkan variable independent (Feature) :
Menyiapkan feature dengan mencari korelasi antara pertanyaan
Karena dataset merupakan quisoner, kami mengeneralisasikan quisoner teresbut dengan mencari kesamaaan topik antara dua set pertanyaan
- Menyiapkan dataset. Dataset ada dua :
Jurnal P Q1 : Dataset on online impulsive buying behavior
of buy now pay later users and non-buy now pay later users in Indonesia using the stimulus-organism-response model
Jurnal M Q1 : Mobile app impulsive buying: A situational factors dataset analysis
- Cleaning data beserta transformasi data ke variable independen yang sudah disiapkan


## Pelengkapan data
#### Tahapan 1 : 
Data jurnal Q1 Mobile tidak memiliki gender dan umur pada raw dataset, kami menggunakan distribusi sesuai persebaran data yang sudah dipaparkan oleh pembuat jurnal. Data tidak 100% akurat namun memberikan persebaran yang cukup 
Breakdown tahapan 1 :
**cjma.py**
- Load dataset
- Check ukuran dataset
- Set proporsi Gender dan umur
- Set gender dengan random
- Verifikasi isi data
- Buat .csv baru (testj3.csv)
#### Tahapan 2 :
Data jurnal Q1 Paylater menggunakan gender 1 dan 2 serta tidak memiliki umur, hanya tahun lahir. Kami mengubah gender dengan 0-1 dan mengubah tahun lahir menjadi grup umur
Breakdown tahapan 2 :
**cjpl.py**
- Edit excel, ganti tahun lahir menjadi umur dengan matematika tanggal dan ganti gender dengan if
- Ubah excel menjadi .csv
- Load dataset
- Ubah umur dengan algoritma
- Verifikasi isi data
- Buat .csv baru (testp1.csv)
Dengan begini data sudah siap untuk digunakan, namun data akan ditransformasi menjadi bentuk yang dapat digunakan

## Transformasi Data
#### Tahapan 1 : 
Data jurnal Mobile akan dikonversi
Gender, Grup Umur, Spontanitas, Pengaruh Sosial, Kesenangan, Rasionalitas
Breakdown tahapan 1 :
**tjma.py**
- Load dataset
- Hitung median dari kolom yang digabungkan lalu dibuat ke kolom baru. (Ada dua pertimbangan yaitu yang pertama memakai average dengan threshold binning, namun karena kestabilan median kami menggunakan median untuk merepresentasikan grup )
- Buat dataset baru hanya dengan kolom yang dipilih
- Verifikasi isi data
- Buat .csv baru (tranjma2.csv)
#### Tahapan 2 :
Data jurnal Paylater akan dikonversi
Gender, Grup Umur, Spontanitas, Pengaruh Sosial, Kesenangan, Rasionalitas
Breakdown tahapan 2 :
**tjml.py**
- Load dataset
- Hitung median dari kolom yang digabungkan lalu dibuat ke kolom baru.
- Buat dataset baru hanya dengan kolom yang dipilih
- Verifikasi isi data
- Buat .csv baru (tranjpl1.csv)
#### Tahap 3 : 
Penggabungan kedua dataset beserta penghilangan nilai desimal
Breakdown Tahapan 3 :
**cbndf.py**
- Load Dataset
- Concat Dataset + remove dupe (optional)
- Verifikasi isi data
- Buat .csv baru (cbndf1.csv)
**clsdf.py**
- Load Dataset
- Membulatkan nilai dengan round
- Verifikasi isi data
- Buat .csv baru (clsdf1.csv)
#### Tahap 4 : 
Pengubahan Rasionalitas menjadi Irasionalitas
**correction.py**
- Load Dataset
- Irasionalitas = 6 - [Nilai Rasionalitas]
- Verifikasi isi data
- Buat .csv baru (revdata1.csv)
#### Tahap 5 :
Pembuatan Label Impulse Buying
**thresholdcustom.py**
- Load Dataset
- Tentukan threshold impulse buying
- Hitung nilai rata-rata label
- Klasifikasikan nilai rata-rata label berdasarkan threshold
- Verifikasi isi data
- Buat .csv baru (datahasil6.csv dan datahasil7.csv)

## Model dan Evaluasi
Silahkan cek `Model Regresi Logistik (Complete).xlsx` di model>excel untuk versi Excel dan `fixmodel2273Compile.exe` juga `fixmodel4456Compile.exe` di model>build untuk versi aplikasi yang bisa langsung dijalankan.