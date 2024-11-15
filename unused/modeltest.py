# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load your dataset (assuming it's a CSV file)
dataset = pd.read_csv('D:/ML/dataset_hasil.csv')

# Prepare the dataset for logistic regression
X = dataset[['Gender', 'Grup Umur', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Rasionalitas']]
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
        'Grup Umur': [age_group],
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

