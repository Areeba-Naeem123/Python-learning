# task 1 

# step 1
#=============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# step 2
#=============================================================
np.random.seed(47)

# Generate synthetic data
num_samples = 1000  

area = np.random.randint(500, 5001, size=num_samples)

bedrooms = np.random.randint(1, 6, size=num_samples)

location = np.random.choice([0, 1], size=num_samples)

price_category = np.random.choice(
    ['low', 'medium', 'high'],
    size=num_samples,
    p=[0.4, 0.4, 0.2]  
)
# DataFrame
df = pd.DataFrame({
    'Area': area,
    'Bedrooms': bedrooms,
    'Location': location,
    'PriceCategory': price_category
})
print ("==========================Data Frame ==============================")
print(df)

# step 3
#=============================================================
#spliting , standardization 
X = df[['Area', 'Bedrooms', 'Location']]  
y = df['PriceCategory']  

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("Training features:\n", X_train)
print("Testing features:\n", X_test)
print("Training labels:\n", y_train)
print("Testing labels:\n", y_test)

# step 4
#=============================================================
#trainng 

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

# Step 5
#=============================================================
#predicting 
y_pred = knn.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
# Step 6
#=============================================================
#Visualization 

k_values = list(range(1, 21))  
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = classification_report(y_test, y_pred, output_dict=True)['accuracy']
    accuracies.append(accuracy)

# Plotting the results
plt.plot(k_values, accuracies, marker='o', color='b', linestyle='-', markersize=6)
plt.title('KNN Accuracy vs. Number of Neighbors (k) \n For Task 2', fontsize=14)
plt.xlabel('Number of Neighbors (k)', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.grid(True)
plt.show()








#=========================================TASK 2==============================================
print("=========================================TASK 2==============================================")
#=========================synthetic data ===============
np.random.seed(18)
# Features
age = np.random.randint(18, 81, num_samples)  
contract_type = np.random.choice([0, 1, 2], size=num_samples)
tenure = np.random.randint(1, 73, num_samples)  
monthly_charges = np.random.randint(20, 121, num_samples) 
total_charges = monthly_charges * tenure 
tech_support = np.random.choice([0, 1], size=num_samples)
internet_service = np.random.choice([0, 1], size=num_samples) 

churn = np.random.choice([0, 1], size=num_samples, p=[0.7, 0.3]) 

# DataFrame
df = pd.DataFrame({
    'Age': age,
    'Contract_Type': contract_type,
    'Tenure': tenure,
    'Monthly_Charges': monthly_charges,
    'Total_Charges': total_charges,
    'Tech_Support': tech_support,
    'Internet_Service': internet_service,
    'Churn': churn
})

df.to_csv("telecom_customer_churn.csv", index=False)

print(df)

#==============================preprocessing data======================

X = df[['Age', 'Contract_Type', 'Tenure', 'Monthly_Charges', 'Total_Charges', 'Tech_Support', 'Internet_Service']]
y = df['Churn']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print(f"Training Features: {X_train.shape}")
print(f"Test Features: {X_test.shape}")
print(f"Training Labels: {y_train.shape}")
print(f"Test Labels: {y_test.shape}")
#==============================training model======================


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

#==============================prediction======================
y_pred = knn.predict(X_test)

print("Classification Report:\n", classification_report(y_test, y_pred))


#==============================visualization======================

k_values = list(range(1, 21))
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = classification_report(y_test, y_pred, output_dict=True)['accuracy']
    accuracies.append(accuracy)

plt.plot(k_values, accuracies, marker='o', color='b', linestyle='-', markersize=6)
plt.title('KNN Accuracy vs. Number of Neighbors (k)\n For Task 2', fontsize=14)
plt.xlabel('Number of Neighbors (k)', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.grid(True)
plt.show()


