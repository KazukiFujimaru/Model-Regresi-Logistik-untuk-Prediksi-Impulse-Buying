# Panduan Parameter Impulse Buying

Berikut ini adalah panduan mengenai parameter-parameter yang digunakan dalam analisis *impulse buying*.

---

### 1. Gender
   - **Deskripsi**: Jenis kelamin responden.
   - **Nilai**:
     - `0`: Laki-laki
     - `1`: Perempuan

### 2. Grup Umur
   - **Deskripsi**: Kategorisasi umur responden.
   - **Nilai**:
     - Umur 18 - 25 : `0`
     - Umur 26 - 30 : `1`
     - Umur 31 - 35 : `2`
     - Umur 36 - 40 : `3`
     - Umur 41 - 45 : `4`
     - Umur 46 - 50 : `5`
     - Umur 51 - 55 : `6`
     - Umur 56 - 60 : `7`

### 3. Spontanitas (*Impulse Buying Tendency*) dalam Berbelanja
   - **Deskripsi**: Menggambarkan kecenderungan seseorang untuk membeli sesuatu yang sebenarnya tidak diperlukan atau hanya karena keinginan belaka.
   - **Sumber**: Jurnal M (bagian IB), Jurnal P (bagian IBB)
   - **Korelasi**: Nilai IB dan IBB menunjukkan tingkat *impulse buying*.
   - **Nilai**: Skala 1 hingga 5, di mana `1` berarti "sangat tidak setuju" dan `5` berarti "sangat setuju."

### 4. Pengaruh Sosial (*Social Influence*) dalam Berbelanja Online
   - **Deskripsi**: Mengukur sejauh mana seseorang terpengaruh oleh orang-orang di sekitar yang juga berbelanja online.
   - **Sumber**: Jurnal M (bagian SE), Jurnal P (bagian SI)
   - **Korelasi**: Nilai SE dan SI mengindikasikan tingkat pengaruh sosial dalam berbelanja online.
   - **Nilai**: Skala 1 hingga 5, di mana `1` berarti "sangat tidak setuju" dan `5` berarti "sangat setuju."

### 5. Kesenangan (*Hedonic Tendency*) dalam Berbelanja Online
   - **Deskripsi**: Menggambarkan perasaan positif atau eskapisme yang dialami saat berbelanja online.
   - **Sumber**: Jurnal M (bagian HB), Jurnal P (bagian H)
   - **Korelasi**: Nilai HB dan H berkaitan dengan aspek hedonisme.
   - **Nilai**: Skala 1 hingga 5, di mana `1` berarti "sangat tidak setuju" dan `5` berarti "sangat setuju."

### 6. Rasionalitas (*Rational Decision Making*) dalam Berbelanja Online
   - **Deskripsi**: Menilai apakah seseorang berbelanja online secara rasional.
   - **Sumber**: Jurnal M (bagian UB), Jurnal P (bagian NE)
   - **Korelasi**: Nilai UB terkait dengan kebutuhan yang logis, dan NE menunjukkan kecenderungan keputusan rasional.
   - **Nilai**: Skala 1 hingga 5, di mana `1` berarti "sangat tidak setuju" dan `5` berarti "sangat setuju."

### 7. Irasionalitas (*Irrational Decision Making*) dalam Berbelanja Online
   - **Deskripsi**: Mengukur kecenderungan berbelanja secara tidak rasional atau tanpa banyak pertimbangan.
   - **Sumber**: Konversi dari nilai Rasionalitas.
   - **Nilai**: Skala 1 hingga 5, di mana `1` berarti "sangat tidak setuju" dan `5` berarti "sangat setuju."

---

## Catatan

- **Pembentukan Variabel Independen**:
  Beberapa nilai pada dataset tidak digunakan karena tidak memiliki korelasi yang kuat. Variabel independen diambil berdasarkan korelasi tinggi antara data pada Jurnal M dan Jurnal P.

- **Grup Umur**:
  Umur dikategorikan ke dalam *Grup Umur* karena Jurnal M menggunakan pengelompokan umur tersebut. Penggunaan nilai umur langsung akan menyulitkan konversi data dari Jurnal M.

- **Rasionalitas ke Irasionalitas**:
  Rasionalitas dikonversi menjadi Irasionalitas karena model performa yang lebih sesuai.

---

## Pertimbangan Nilai Tambahan

1. **Self Control** dapat dimasukkan ke dalam kategori Rasionalitas.
2. **Physical Environment** dan **Time Perspective** dapat digabungkan menjadi *Kemudahan (Ease of Use)*, serta digabungkan dengan *Promosi E-Paylater* di bawah topik kemudahan berbelanja.

---

## Dataset Eksperimen dan Masalah yang Ditemui

Eksperimen data:
- `datahasil1`: Rasionalitas *k-means*
- `datahasil2`: Rasionalitas *threshold*
- `datahasil3`: Irasionalitas *threshold* 3.0
- `datahasil4`: Irasionalitas *threshold* 2.7
- `datahasil5`: Irasionalitas *k-means*
- `datahasil6`: Irasionalitas *Custom threshold* rasio 27:73
- `datahasil8`: Irasionalitas *Custom threshold* rasio 44:56

### Masalah yang Ditemui
1. *datahasil1* dan *datahasil2* masih menggunakan *Rasionalitas*.
2. *Gender* dan *Grup Umur* tidak memiliki nilai komposit di *datahasil3* dan *datahasil4*.
3. Pada *datahasil 5* *Klasifikasi* terlalu fokus pada *Gender* dan tidak mencakup variabel lain.

datahasil1 rasionalitas k-mean 
datahasil2 rasionalitas threshold
datahasil3 fix threshold 3.0
datahasil4 fix threshold 2.7
datahasil5 fix k-mean
datahasil6 fix custom threshold dengan rasio 27:73
datahasill8 fix custom threshold dengan rasio 44:56

Problem
1 dan 2 rasionalitas salah
3 dan 4 gender dan umur tidak punya value
5 klasifikasi focus pada gender dan tidak value lain