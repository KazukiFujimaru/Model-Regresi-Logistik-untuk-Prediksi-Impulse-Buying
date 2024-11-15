import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, classification_report, accuracy_score

# Load your dataset (assuming it's a CSV file)
# Replace 'your_dataset.csv' with the actual path to your dataset file
dataset = pd.read_csv('D:ML/datahasil1.csv')

# Prepare the dataset for logistic regression
X = dataset[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Rasionalitas']]
y = dataset['Impulse Buying']  # Make sure you have this column

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = log_reg.predict(X_test)

# Getting the predicted probabilities for the positive class
y_scores = log_reg.predict_proba(X_test)[:, 1]  

# Calculate ROC curve and AUC
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

# Plotting the ROC curve
plt.figure()
plt.plot(fpr, tpr, color='blue', label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='red', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.show()

# Finding the best threshold
optimal_idx = np.argmax(tpr - fpr)  # This finds the threshold that maximizes the difference
optimal_threshold = thresholds[optimal_idx]
print(f'Optimal Threshold: {optimal_threshold}')

# Print classification report and accuracy for reference
print(classification_report(y_test, y_pred))
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
