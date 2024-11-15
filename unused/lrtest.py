# Import the required libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load your dataset (assuming it's in a CSV format)
df = pd.read_csv('D:/ML/datahasil2.csv')

# Display the first few rows of the data
print(df.head())

# Define your features (X) and target (y)
X = df[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Rasionalitas']]  # Independent variables
y = df['Impulse Buying']  # Dependent variable (target)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Output the shapes to check
print(X_train.shape, X_test.shape)

# Initialize the logistic regression model
log_reg = LogisticRegression()

# Train the model on the training data
log_reg.fit(X_train, y_train)

# Predict the labels on the test set
y_pred = log_reg.predict(X_test)

# Print the predictions
print(y_pred)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Print a classification report
print(classification_report(y_test, y_pred))

# Optional: Tune the model by using regularization
log_reg = LogisticRegression(C=0.8)
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(classification_report(y_test, y_pred))

# Function to predict impulse buying on new data
def predict_impulse_buying(model, scaler):
    # Input new data for prediction
    print("Please input the following details for prediction:")
    
    # Taking inputs from user
    gender = int(input("Gender (0 for Male, 1 for Female): "))
    age_group = int(input("Age Group (0 to 7): "))
    spontanitas = int(input("Spontanitas (1 to 5): "))
    pengaruh_sosial = int(input("Pengaruh Sosial (1 to 5): "))
    kesenangan = int(input("Kesenangan (1 to 5): "))
    rasionalitas = int(input("Rasionalitas (1 to 5): "))
    
    # Creating a DataFrame for the new input
    new_data = pd.DataFrame({
        'Gender': [gender],
        'Age Group': [age_group],
        'Spontanitas': [spontanitas],
        'Pengaruh Sosial': [pengaruh_sosial],
        'Kesenangan': [kesenangan],
        'Rasionalitas': [rasionalitas]
    })
    
    # Preprocess the input data (scaling)
    new_data_scaled = scaler.transform(new_data)
    
    # Predicting the output using the logistic regression model
    prediction = model.predict(new_data_scaled)
    
    # Output the result
    if prediction == 1:
        print("Prediction: This person is likely to engage in Impulse Buying.")
    else:
        print("Prediction: This person is NOT likely to engage in Impulse Buying.")

# Example of how you might call this function after training your model
# Uncomment to test
# Loop to predict until the user decides to exit
while True:
    predict_impulse_buying(log_reg, scaler)
    
    # Ask the user if they want to make another prediction
    continue_prompt = input("Do you want to make another prediction? (y/n): ").strip().lower()
    if continue_prompt != 'y':
        break