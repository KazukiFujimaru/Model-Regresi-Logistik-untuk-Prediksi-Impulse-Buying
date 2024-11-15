# PANDUAN INI HANYA UNTUK SISTEM OPERASI WINDOWS

## MENGGUNAKAN ENVIRONMENT
#### 1. Unduh kode sumber beserta environment (AIS3)
#### 2. Simpan kode sumber dan environment 
#### 3. Buka command prompt dan pergi ke path dimana AIS3 diunduh 
Contohnya  di PC saya AIS3 ada di partisi D dan folder ML sehingga : 

```
D:\> cd D:\ML\Model-Regresi-Logistik-untuk-Prediksi-Impulse-Buying>
```
Hasilnya :

```
D:\ML\Model-Regresi-Logistik-untuk-Prediksi-Impulse-Buying>
```

#### 4. Aktifkan environment
Dapat dilakukan dengan mengetik perintah berikut di CMD :
```
AIS3\Scripts\activate.bat
```
Contoh :
```
D:\ML\Model-Regresi-Logistik-untuk-Prediksi-Impulse-Buying> AIS3\Scripts\activate.bat
```

Setelah berhasil akan ada tulisan AIS3 dibelakang path :
```
(AIS3) D:\ML\Model-Regresi-Logistik-untuk-Prediksi-Impulse-Buying>
```

#### 5. Jalankan kode 
Untuk menjalankan kode, masukan perintah berikut ke CMD :
```
python .\kode+data\kode_sumber_model\fixmodel2773.py
```

Contoh :
```
(AIS3) D:\ML\Model-Regresi-Logistik-untuk-Prediksi-Impulse-Buying>python .\kode+data\kode_sumber_model\fixmodel2773.py
```

Kode akan berjalan jika semua langkah dilakukan secara benar.

---

## MENGGUNAKAN LIBRARY 
(METODE INI TIDAK DISARANKAN KECUALI JIKA KITA MEMBUAT ENVIRONMENT BARU TERLEBIH DAHULU)
(METODE INI DIGUNAKAN JIKA LIBRARY INGIN DIGUNAKAN SERING DAN DIINSTALL SECARA GLOBAL [PADA ROOT])

#### 1. Unduh dan install PIP (https://pip.pypa.io/en/stable/installation/). Pastikan PIP terinstall
#### 2. Download Library yang dibutuhkan dengan pip
Masukan perintah berikut di cmd :
```
pip install pandas numpy scikit-learn customtkinter matplotlib
```
#### 3. Tunggu instalasi selesai
#### 4. Jalankan kode python menggunakan VS Code atau CMD
Jika CMD digunakakn, masukan perintah berikut ke CMD :
```
python path\untuk\model\regresilogistik
```

Contoh :
```
python "D:\ML\Model-Regresi-Logistik-untuk-Prediksi-Impulse-Buying\kode+data\kode_sumber_model\fixmodel2773.py"
```

Kode akan berjalan jika semua langkah dilakukan secara benar.