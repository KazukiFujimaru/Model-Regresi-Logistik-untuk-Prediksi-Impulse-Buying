# Import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.preprocessing import StandardScaler, PolynomialFeatures 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score


# Load your dataset (assuming it's a CSV file)
dataset = pd.read_csv('D:\ML\datahasil6.csv')

# Prepare the dataset for logistic regression
X = dataset[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas']]
y = dataset['Impulse Buying']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a logistic regression model
log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = log_reg.predict(X_test_scaled)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Get the intercept (β₀)
intercept = log_reg.intercept_[0]
print(f'Intercept (β₀): {intercept}')

# Get the coefficients (β₁, β₂, ..., βₙ)
coefficients = log_reg.coef_[0]
print(f'Coefficients: {coefficients}')

# Get feature importance (coefficients)
feature_importance = log_reg.coef_[0]
print(f'Feature Importance: {feature_importance}')

# Check for correlations
correlation_matrix = dataset[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas']].corr()
print(correlation_matrix)



def predict_impulse_buying(model, scaler, input_data):
    # Preprocess the input data (scaling)
    new_data_scaled = scaler.transform(input_data)
    
    # Predicting the output using the logistic regression model
    prediction = model.predict(new_data_scaled)
    
    return prediction[0]  # Return the prediction

def on_predict():
    # Getting user inputs from the GUI
    gender = int(gender_entry.get())
    age_group = int(age_group_entry.get())
    spontanitas = int(spontanitas_entry.get())
    pengaruh_sosial = int(pengaruh_sosial_entry.get())
    kesenangan = int(kesenangan_entry.get())
    rasionalitas = int(rasionalitas_entry.get())
    
    # Creating a DataFrame for the new input
    new_data = pd.DataFrame({
        'Gender': [gender],
        'Age Group': [age_group],
        'Spontanitas': [spontanitas],
        'Pengaruh Sosial': [pengaruh_sosial],
        'Kesenangan': [kesenangan],
        'Irasionalitas': [rasionalitas]
    })
    
    # Get prediction
    prediction = predict_impulse_buying(log_reg, scaler, new_data)
    
    # Display result in a message box
    if prediction == 1:
        messagebox.showinfo("Prediction Result", "This person is likely to engage in Impulse Buying.")
    else:
        messagebox.showinfo("Prediction Result", "This person is NOT likely to engage in Impulse Buying.")

# Creating the main window
root = tk.Tk()
root.title("Impulse Buying Prediction")

# Creating input fields
tk.Label(root, text="Gender (0 for Male, 1 for Female):").grid(row=0, column=0)
gender_entry = tk.Entry(root)
gender_entry.grid(row=0, column=1)

tk.Label(root, text="Age Group (0 to 7):").grid(row=1, column=0)
age_group_entry = tk.Entry(root)
age_group_entry.grid(row=1, column=1)

tk.Label(root, text="Spontanitas (1 to 5):").grid(row=2, column=0)
spontanitas_entry = tk.Entry(root)
spontanitas_entry.grid(row=2, column=1)

tk.Label(root, text="Pengaruh Sosial (1 to 5):").grid(row=3, column=0)
pengaruh_sosial_entry = tk.Entry(root)
pengaruh_sosial_entry.grid(row=3, column=1)

tk.Label(root, text="Kesenangan (1 to 5):").grid(row=4, column=0)
kesenangan_entry = tk.Entry(root)
kesenangan_entry.grid(row=4, column=1)

tk.Label(root, text="Irasionalitas (1 to 5):").grid(row=5, column=0)
rasionalitas_entry = tk.Entry(root)
rasionalitas_entry.grid(row=5, column=1)

# Predict button
predict_button = tk.Button(root, text="Predict", command=on_predict)
predict_button.grid(row=6, columnspan=2)

# Start the GUI event loop
root.mainloop()
