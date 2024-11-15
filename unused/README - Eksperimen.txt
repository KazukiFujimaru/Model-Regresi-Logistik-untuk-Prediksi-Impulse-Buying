Berikut adalah penjelasan dari tiap file yang tidak terpakai dan mengapa file tersebut tidak dipakai lagi :

Diurutkan secara urutan prosedur

Pelengkapan jurnal M
testj1.csv - Ada kesalahan dalam kategori pelabelan
testj2.csv - Rasio pelabelan gender dan umur belum akurat

Pelengkapan jurnal P
Raw_Data_PayLater Non CSV.csv - Data sudah berbentuk tabel, belum memiliki koma walaupun bentuknya csv. Ketika di run berkemungkinan error.
Test.xlsx - Mengubah Raw_Data_Paylater menjadi bentuk tabel di Excel

Transformasi jurnal M
tranjma1.csv - nilai belum dikonversi menjadi label yang sudah ditentukan

Transformasi jurnal p
tidak ada

Model dengan dataset lengkap
Raw_Data_IB.csv - Isinya sama dengan clsdf1, awalnya digunakan untuk model. Disini belum ada label Impulse Buying. Label Rasionalitas masih ada
Raw_Data_IB.xlsx - adalah clsdf1 namun berbentuk excel, awalnya digunakan untuk model. Disini belum ada label Impulse Buying. Label Rasionalitas masih ada
kmeanlabel.py - dipakai untuk menghasilkan datahasil1 dan datahasil5. Menggunakan metode K-Mean untuk membuat label pada dataset.
datahasil1.csv - dataset dari Raw_Data_IB yang ditambahkan label Impulse Buying menggunakan metode K-Mean. Label Rasionalitas masih ada
threshold label.py - Digunakan untuk datahasil2, datahasil3, dan datahasil4. Pelabelan Impulse Buying menggunakan nilai patokan tetap yang dapat ditentukan
datahasil2.csv - dataset dari Raw_Data_IB yang ditambahkan label Impulse Buying menggunakan threshold. Label Rasionalitas masih ada
lrtest.py - digunakan pada datahasil2.csv untuk ujicoba model regresi logistik
lrtest2.py - digunakan pada datahasil1.csv untuk ujicoba model regresi logistik
kmlrtest.py - uji coba model regresi logistik dengan menerapkan k-mean langsung pada proses. Dataset yang digunakan adalah Raw_Data_IB.csv dan label Impulse Buying diterapkan langsung melalui k-mean ketika kode berjalan
threshold optimal.py - Digunakan pada datahasil1. Penggunaan metode penentuan nilai patokan optimal yang paling baik menggunakan matplotlib. Namun metode ini tidak efektif.
dataset_hasil.csv - dataset dari Raw_data_IB yang ditambahkan label dengan menggunakan threshold. Nilai threshold disini diambil dari threshold optimal.csv Label Rasionalitas masih ada
modeltest.py - digunakan pada dataset_hasil.csv untuk ujicoba model regresi logistik
modeltestGUI.py - digunakan pada dataset_hasil.csv untuk ujicoba model regresi logistik menggunakan tkinter GUI.
datahasil3.csv - dataset dari revdata1.csv namun menggunakan threshold tetap 3.0 untuk pelabelan Impulse Buying
datahasil4.csv - dataset dari revdata1.csv namun menggunakan threshold tetap 2.7 untuk pelabelan Impulse Buying
datahasil5.csv -  dataset dari revdata1.csv namun menggunakan K-Mean untuk pelabelan Impulse Buying
revdataGUI.py - digunakan pada datahasil6.csv untuk ujicoba model regresi logistik menggunakan tkinter GUI.


