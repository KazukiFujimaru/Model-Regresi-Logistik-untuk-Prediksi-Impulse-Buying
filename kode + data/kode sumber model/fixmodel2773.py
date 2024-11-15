# JIKA KODE TIDAK BERJALAN, SILAHKAN INSTALL LIBRARY PYTHON YANG SESUAI DAN DIREKTORI LOAD DATASET SESUAI

# Tahap 1 : Import library
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # data visualization
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk

# Tahap 2 : Load Dataset
df = pd.read_csv('datahasil6.csv')

# Opsional, pengecekan info dataset
print("Berikut informasi tentang data :")
print(df.shape)
print(df.head())
print(df.columns)
print(df.info())

# Opsional, pengecekan variabel
numerical = [var for var in df.columns if df[var].dtype!='O']
print('Ada {} variabel\n'.format(len(numerical)))
print('Variabel tersebut adalah :', numerical)
print(df[numerical].isnull().sum()) # Mengecek jika ada data yang kosong (perlu perbaikan)

# Bagusnya ada pengecekan distribusi data menggunakan matplotlib (Eksplorasi data)

# Tahap 3 : Deklarasi Variabel
X = df[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas']]
y = df['Impulse Buying']

# Tahap 4 : Deklarasi model
from sklearn.model_selection import train_test_split # Import sklearn
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) #Command training

# Opsional, cek jumlah data yang digunakan untuk latihan model dan testing model
print(X_train.shape)
print(X_test.shape)

# Tahap sesudah ini seharusnya adalah Feature Engineering dimana kekurangan dataset diatasi dan diperbaiki
# Feature Engineering adalah tahap pembersihan data beserta visualisasi data

# Tahap 5 : Feature Scaling
from sklearn.preprocessing import MinMaxScaler
cols = X_train.columns
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train = pd.DataFrame(X_train, columns=[cols])
X_test = pd.DataFrame(X_test, columns=[cols])
print("\nSetelah scaling, data berubah seperti ini :")
print(X_train.describe())

# Tahap 6 : Model training
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='liblinear', random_state=0)
logreg.fit(X_train, y_train)

# Opsional, prediksi hasil
y_pred_test = logreg.predict(X_test)
print("Tes Prediksi")
print(y_pred_test)

# Tahap 7 : Pengecekan performa :
#  1. Akurasi model
print("\nBerikut pengecekan performa dari model yang ada :")
from sklearn.metrics import accuracy_score
print('Skor akurasi model: {0:0.4f}'. format(accuracy_score(y_test, y_pred_test)))
y_pred_train = logreg.predict(X_train)
print('Skor akurasi set latihan: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train)))
print('Skor akurasi set testing: {:.4f}'.format(logreg.score(X_test, y_test)))
# Pengecekan Overfitting dan Underfitting.. C adalah kekuatan regularisasi
logreg100 = LogisticRegression(C=100, solver='liblinear', random_state=0)
logreg100.fit(X_train, y_train)
print("\nAkurasi dengan regularisasi data lemah :") #Model lebih sesuai dengan data latihan
print('Skor akurasi set latihan: {:.4f}'.format(logreg100.score(X_train, y_train)))
print('Skor akurasi set testing: {:.4f}'.format(logreg100.score(X_test, y_test)))
logreg001 = LogisticRegression(C=0.01, solver='liblinear', random_state=0)
logreg001.fit(X_train, y_train)
print("\nAkurasi dengan regularisasi data kuat :") #Model harus lebih generalisasi data
print('Skor akurasi set latihan: {:.4f}'.format(logreg001.score(X_train, y_train)))
print('Skor akurasi set testing: {:.4f}'.format(logreg001.score(X_test, y_test)))
#Pengecekan akurasi null
print("\nCek akurasi null :") #Yaitu akurasi dari kelas yang paling banyak di prediksi
print(y_test.value_counts())
null_accuracy = (158/(158+130))
print('Null accuracy score: {0:0.4f}'. format(null_accuracy)) #Artinya model belajar dengan baik dan bukan ditentukan dari mayoritas data

# 2. Cofusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred_test)
print('\nConfusion matrix\n\n', cm)
print('\nTrue Positives(TP) = ', cm[0,0]) #Prediksi 1, data asli 1
print('True Negatives(TN) = ', cm[1,1]) #Prediksi 0, data asli 0
print('False Positives(FP) = ', cm[0,1]) #Prediksi 1, data asli 0
print('False Negatives(FN) = ', cm[1,0]) #Prediksi 0, data asli 1

# 3. Laporan Klasifikasi
# Laporan Klasifikasi
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred_test)) #f1-score adalah gabungan presisi dan recall
# Akurasi Klasifikasi
TP = cm[0,0]
TN = cm[1,1]
FP = cm[0,1]
FN = cm[1,0]
classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Akurasi Klasifikasi : {0:0.4f}'.format(classification_accuracy)) # Total benar
classification_error = (FP + FN) / float(TP + TN + FP + FN)
print('Error Klasifikasi : {0:0.4f}'.format(classification_error)) # Total salah
precision = TP / float(TP + FP)
print('Presisi : {0:0.4f}'.format(precision)) # Tingkat ketepatan prediksi
recall = TP / float(TP + FN)
print('Recall atau Sensitivity : {0:0.4f}'.format(recall)) # Tingkat kesesuaian prediksi benar dengan data asli
specificity = TN / (TN + FP)
print('Specificity : {0:0.4f}'.format(specificity)) # Tingkat kesesuaian prediksi salah dengan data asli
true_positive_rate = TP / float(TP + FN)
print('True Positive Rate : {0:0.4f}'.format(true_positive_rate)) # True Positive
false_positive_rate = FP / float(FP + TN)
print('False Positive Rate : {0:0.4f}'.format(false_positive_rate)) # True Negative

# 4. Cek korelasi, intercept, coefficient
print("Korelasi antar data seperti berikut :")
print(df.corr())
intercept = logreg.intercept_
coefficients = logreg.coef_
print("Intercept:", intercept)
print("Coefficients:", coefficients)


# Sebenarnya masih ada tahapan lagi namun karena model dirasa cukup, saya cukupkan sekian.
# Tahapan-tahapan yang tidak saya lakukan adalah
# 1. Penyesuaian Threshold
# 2. ROC-AUC
# 3. k-Fold Cross Validation
# 4. Hyperparameter Optimization using GridSearch CV

# ROC-AUC (Receiver Operating Characteristic - Area Under Curve)
# An ROC Curve is a plot which shows the performance of a classification model at various classification threshold levels.
# AUC is a technique to compare classifier performance. 
# In this technique, we measure the area under the curve (AUC). 
# A perfect classifier will have a ROC AUC equal to 1, whereas a purely random classifier will have a ROC AUC equal to 0.5.
# ROC AUC is a single number summary of classifier performance. The higher the value, the better the classifier.

from sklearn.metrics import roc_curve
y_pred1 = logreg.predict_proba(X_test)[:,1]
y_pred1 = y_pred1.reshape(-1,1)
fpr, tpr, thresholds = roc_curve(y_test, y_pred1)
plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, linewidth=2)
plt.plot([0,1], [0,1], 'k--' )
plt.rcParams['font.size'] = 12
plt.title('ROC curve for Impulse Buying')
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.show()
from sklearn.metrics import roc_auc_score
ROC_AUC = roc_auc_score(y_test, y_pred1)
print('ROC AUC : {:.4f}'.format(ROC_AUC))

# Poin sesudah ini adalah untuk pembuatan GUI
# GUI adalah Graphical User Interface, yaitu antarmuka pengguna yang dapat digunakan 
# untuk berinteraksi dengan sistem komputer.

def predict_impulse_buying(model, scaler, input_data):
    # Preprocess the input data (scaling)
    new_data_scaled = scaler.transform(input_data)
    
    # Predicting the output using the logistic regression model
    prediction = model.predict(new_data_scaled)
    
    return prediction[0]  # Return the prediction

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# GUI Config
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Model Regresi Logistik Impulse Buying")
        self.geometry(f"400x300")

        # configure grid layout (2x6)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        # History Declaration
        self.history = []

        # Creating input fields
        self.gender_label = ctk.CTkLabel(self, text="Gender (0 untuk Pria, 1 untuk Wanita):")
        self.gender_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.gender_entry = ctk.CTkEntry(self)
        self.gender_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        self.age_group_label = ctk.CTkLabel(self, text="Grup Umur (0 sampai 7):")
        self.age_group_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.age_group_entry = ctk.CTkEntry(self)
        self.age_group_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.spontanitas_label = ctk.CTkLabel(self, text="Spontanitas (1 sampai 5):")
        self.spontanitas_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.spontanitas_entry = ctk.CTkEntry(self)
        self.spontanitas_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        self.pengaruh_sosial_label = ctk.CTkLabel(self, text="Pengaruh Sosial (1 sampai 5):")
        self.pengaruh_sosial_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.pengaruh_sosial_entry = ctk.CTkEntry(self)
        self.pengaruh_sosial_entry.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        self.kesenangan_label = ctk.CTkLabel(self, text="Kesenangan (1 sampai 5):")
        self.kesenangan_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.kesenangan_entry = ctk.CTkEntry(self)
        self.kesenangan_entry.grid(row=4, column=1, padx=20, pady=10, sticky="ew")

        self.irasionalitas_label = ctk.CTkLabel(self, text="Irasionalitas (1 sampai 5):")
        self.irasionalitas_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.irasionalitas_entry = ctk.CTkEntry(self)
        self.irasionalitas_entry.grid(row=5, column=1, padx=20, pady=10, sticky="ew")

        # Predict button
        self.predict_button = ctk.CTkButton(self, text="Prediksi", command=self.on_predict)
        self.predict_button.grid(row=6, column=0, padx=20, pady=5, sticky="ew")

        # History button
        self.history_button = ctk.CTkButton(self, text="History", command=self.show_history)
        self.history_button.grid(row=6, column=1, padx=20, pady=5, sticky="ew")

    def on_predict(self):
        # Get input value
        gender = self.gender_entry.get()
        age_group = self.age_group_entry.get()
        spontanitas = self.spontanitas_entry.get()
        pengaruh_sosial = self.pengaruh_sosial_entry.get()
        kesenangan = self.kesenangan_entry.get()
        irasionalitas = self.irasionalitas_entry.get()

        # Empty value handling
        if not gender or not age_group or not spontanitas or not pengaruh_sosial or not kesenangan or not irasionalitas:
            messagebox.showerror("Input Error", "Tolong isi semua data dengan")
            return  # Stop the function if validation fails

        # Value verification and error checking
        try:
            gender = int(gender)
            age_group = int(age_group)
            spontanitas = int(spontanitas)
            pengaruh_sosial = int(pengaruh_sosial)
            kesenangan = int(kesenangan)
            irasionalitas = int(irasionalitas)

            # Check if values are within the expected ranges
            if gender not in [0, 1]:
                raise ValueError("Gender harus 0 (Pria) atau 1 (Wanita).")
            if not (0 <= age_group <= 7):
                raise ValueError("Grup Umur harus satu angka diantara 0 sampai 7.")
            if not (1 <= spontanitas <= 5):
                raise ValueError("Spontanitas harus satu angka diantara 1 sampai 5.")
            if not (1 <= pengaruh_sosial <= 5):
                raise ValueError("Pengaruh Sosial harus satu angka diantara 1 sampai 5.")
            if not (1 <= kesenangan <= 5):
                raise ValueError("Kesenangan harus satu angka diantara 1 sampai 5.")
            if not (1 <= irasionalitas <= 5):
                raise ValueError("Irasionalitas harus satu angka diantara 1 sampai 5.")

        except ValueError as e:
            # If the input is not valid or out of range, display an error message
            messagebox.showerror("Input Error", str(e))
            return

        # Convert df for input
        new_data = pd.DataFrame({
            'Gender': [gender],
            'Age Group': [age_group],
            'Spontanitas': [spontanitas],
            'Pengaruh Sosial': [pengaruh_sosial],
            'Kesenangan': [kesenangan],
            'Irasionalitas': [irasionalitas]
        })

        # Model usage
        prediction = predict_impulse_buying(logreg, scaler, new_data)  # Ensure 'logreg' and 'scaler' are defined

        # Store result in history
        self.history.append({
            'Gender': gender,
            'Age Group': age_group,
            'Spontanitas': spontanitas,
            'Pengaruh Sosial': pengaruh_sosial,
            'Kesenangan': kesenangan,
            'Irasionalitas': irasionalitas,
            'Impulse Buying': "Ya" if prediction == 1 else "Tidak"
        })

        # Display result
        if prediction == 1:
            messagebox.showinfo("Hasil Prediksi", "Data terindikasi masuk Impulse Buying")
        else:
            messagebox.showinfo("Hasil Prediksi", "Data terindikasi TIDAK masuk Impulse Buying")

    def show_history(self):
        # Create a new window for displaying the table
        history_window = tk.Toplevel(self)
        history_window.title("History Prediksi")
        history_window.geometry("1050x400")

        # Create a Treeview widget to display the history as a table
        tree = ttk.Treeview(history_window, columns=('Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas', 'Impulse Buying'), show='headings')
        tree.pack(expand=True, fill='both')

        # Define the column headings
        tree.heading('Gender', text='Gender')
        tree.heading('Age Group', text='Age Group')
        tree.heading('Spontanitas', text='Spontanitas')
        tree.heading('Pengaruh Sosial', text='Pengaruh Sosial')
        tree.heading('Kesenangan', text='Kesenangan')
        tree.heading('Irasionalitas', text='Irasionalitas')
        tree.heading('Impulse Buying', text='Impulse Buying')

        # Adjust column widths
        tree.column('Gender', width=150)
        tree.column('Age Group', width=150)
        tree.column('Spontanitas', width=150)
        tree.column('Pengaruh Sosial', width=150)
        tree.column('Kesenangan', width=150)
        tree.column('Irasionalitas', width=150)
        tree.column('Impulse Buying', width=150)

        # Insert the history data into the table
        for entry in self.history:
            tree.insert('', 'end', values=(entry['Gender'], entry['Age Group'], entry['Spontanitas'], entry['Pengaruh Sosial'], entry['Kesenangan'], entry['Irasionalitas'], entry['Impulse Buying']))

# Run GUI
if __name__ == "__main__":
    app = App()
    app.mainloop()