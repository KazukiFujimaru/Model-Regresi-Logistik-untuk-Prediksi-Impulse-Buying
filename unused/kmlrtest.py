# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load your dataset (assuming it's a CSV file)
# Replace 'your_dataset.csv' with the actual path to your dataset file
dataset = pd.read_csv('D:/ML/Raw_Data_IB.csv')

# Step 1: Select the features for clustering
features = dataset[['Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Rasionalitas']]

# Step 2: Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Step 3: Apply K-Means with 2 clusters (for binary classification)
kmeans = KMeans(n_clusters=2, random_state=42)
dataset['Impulse_Buying_Label'] = kmeans.fit_predict(features_scaled)

# Step 4: Analyze cluster centers to interpret which one represents impulse buying
clustered_data = pd.concat([dataset, pd.DataFrame(features_scaled, columns=['Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Rasionalitas'])], axis=1)

# Inspect mean values for each cluster to determine which is impulse buying
print(clustered_data.groupby('Impulse_Buying_Label').mean())

# (Optional) If necessary, adjust the labels (0 for non-impulse buyer, 1 for impulse buyer)
# Uncomment the following line if needed, after inspecting the mean values.
dataset['Impulse_Buying_Label'] = dataset['Impulse_Buying_Label'].map({0: 1, 1: 0})

# Step 5: Prepare the dataset for logistic regression
# Select features and the newly created label
X = dataset[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Rasionalitas']]
y = dataset['Impulse_Buying_Label']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train a logistic regression model
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Step 7: Make predictions and evaluate the model
y_pred = log_reg.predict(X_test)

# Print accuracy and classification report
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the processed dataset with labels
#dataset.to_csv('D:ML/dataset_hasil.csv', index=False)
#print("Proses berhasil. Sudah disimpan")