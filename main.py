import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 1. Load the dataset
# Make sure USA_Housing.csv is in the same folder as this script!
try:
    df = pd.read_csv('USA_Housing.csv')
    print("Step 1: Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: 'USA_Housing.csv' not found. Please check the file path.")
    exit()

# 2. Preprocessing
# We select only numerical features for this linear regression model
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

# 3. Split the data (60% training, 40% testing to match your previous setup)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# 4. Train the Model
print("Step 2: Training the model...")
lm = LinearRegression()
lm.fit(X_train, y_train)

# 5. Evaluate the Model
predictions = lm.predict(X_test)

print("\n--- MODEL PERFORMANCE ---")
print('MAE (Mean Absolute Error):   $', round(metrics.mean_absolute_error(y_test, predictions), 2))
print('RMSE (Root Mean Squared Error): $', round(np.sqrt(metrics.mean_squared_error(y_test, predictions)), 2))
print('R² Score (Accuracy):        ', round(lm.score(X_test, y_test), 4))

# 6. Understanding the Coefficients (The 'Impact' of each feature)
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print("\n--- FEATURE IMPACT ---")
print(coeff_df)

# 7. Visualizing the Results
print("\nStep 3: Generating graphs... (Close the graph windows to finish)")

# Graph 1: Actual vs Predicted
plt.figure(figsize=(10, 5))
plt.scatter(y_test, predictions, color='blue', edgecolor='white', alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', lw=2) # Ideal line
plt.title('Actual Prices vs. Predicted Prices')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.show()

# Graph 2: Residual Histogram
plt.figure(figsize=(10, 5))
sns.histplot((y_test - predictions), bins=50, kde=True, color='green')
plt.title('Distribution of Errors (Residuals)')
plt.xlabel('Price Difference (Error)')
plt.show()