import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. LOAD THE DATA
data = pd.read_csv('data.csv')
X = data[['Rainfall']] # Independent variable
y = data['Yield']    # Dependent variable

# 2. ANALYSIS (Module 3 Concepts)
print(f"Average Rainfall: {data['Rainfall'].mean():.2f} mm")
print(f"Average Yield: {data['Yield'].mean():.2f} kg")

# 3. TRAIN THE MODEL (Module 4 Concepts)
# We split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train) # This finds the line y = mx + c

# 4. PREDICTION & VISUALIZATION
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title('Rainfall vs Crop Yield')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Yield (kg)')
plt.legend()
plt.show()

# Test the model
val = float(input("Enter expected rainfall (mm) to predict yield: "))
prediction = model.predict([[val]])
print(f"Predicted Yield: {prediction[0]:.2f} kg/hectare")