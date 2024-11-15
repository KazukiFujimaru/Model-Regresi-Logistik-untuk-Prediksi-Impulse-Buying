import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Assuming your dataset is already loaded and looks something like this:
# Gender, Age Group, Spontanitas, Pengaruh Sosial, Kesenangan, Irasionalitas
# For example:
# dataset = pd.read_csv("your_dataset.csv")

# Tahap 1 : Load dataset
dataset = pd.read_csv('D:/ML/revdata1.csv') # File path dataset

# Select features for K-Means Clustering
features = dataset[['Gender', 'Age Group', 'Spontanitas', 'Pengaruh Sosial', 'Kesenangan', 'Irasionalitas']]

# Optionally scale the data (important for K-Means to treat all features equally)
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Initialize K-Means model with 2 clusters (Impulse Buyer, Not Impulse Buyer)
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(features_scaled)

# Add the cluster labels to the dataset
dataset['Cluster_Label'] = kmeans.labels_

# Mapping Cluster labels (optional, depends on how K-Means labels them)
# If necessary, map 0 to "Not Impulse" and 1 to "Impulse"
# This step can be reversed if needed based on cluster output
dataset['Impulse Buying'] = dataset['Cluster_Label'].map({0:0,1:1})

# Display the dataset with the new labels
print(dataset)

# If you want to visualize the clusters (only works if you reduce dimensions)
# This step helps you understand the clusters but is optional
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Reduce dimensions to 2D for visualization purposes
pca = PCA(n_components=2)
features_2d = pca.fit_transform(features_scaled)

# Tahap 5 : Save hasil ke .csv baru
dataset.to_csv('D:/ML/datahasil5.csv', index=False)
print("Proses berhasil : 'D:/ML/datahasil5.csv'")

# Plot the clusters
plt.scatter(features_2d[:, 0], features_2d[:, 1], c=kmeans.labels_, cmap='viridis')
plt.xlabel('PCA Feature 1')
plt.ylabel('PCA Feature 2')
plt.title('K-Means Clustering of Impulse Buying Behavior')
plt.colorbar(label='Cluster Label')
plt.show()