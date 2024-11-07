# # Group Project
# B.Tech - Computer Science and Engineering (DSAI - B)
# Course : Data Science Fundamentals (CS_260)
# Group Members :
# Vivek Kumar - 2300100341
# Vaibhav Chaurasiya - 2300100765
# Rohit Yadav - 2300101185
# Rachit Singh - 2300100328

# # Project Introduction:
# This project aims to analyze a dataset containing height and weight information, 
# obtained in metric units (centimeters for height and kilograms for weight).
# The dataset is sourced from Kaggle, and the main objective is to perform data exploration, 
# handle any missing values, extract meaningful insights, and visualize the data.

# # Project Steps:
# 1. Load and read the dataset using Pandas.
# 2. Handle any missing values to ensure data quality.
# 3. Extract meaningful statistical insights, such as correlation, range, variance, and skewness, 
# to understand the data distribution and variability.
# 4. Visualize the data using Matplotlib to present findings visually.
# Throughout the code, comments will explain each step for clear documentation and easy understanding.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\nProject: Height and Weight Analysis")
print("Objective: Analyze height and weight data to extract insights and visualize patterns.")
print("Steps: Data loading, handling missing values, statistical insights, and visualization.")
print("Dataset: Height (cm) and Weight (kg) sourced from Kaggle")

print("\n - - - - - - - - - - - - - - - - ", end="\n\n")

#
# # Step 1: Dataset Selection
print("\nStep 1: Dataset Selection")
print("We are using a dataset containing height and weight information in metric units.")
print("The dataset is sourced from Kaggle and saved as 'weight_height_metric.csv'.")
print("Columns included in the dataset: Height_cm (in centimeters) and Weight_kg (in kilograms).")

print("\n - - - - - - - - - - - - - - - - ", end="\n\n")

#
# # Step 2: Reading the Dataset using Pandas
print("\nStep 2: Reading the dataset into a DataFrame.")

data = pd.read_csv('weight_height_metric.csv')
df = pd.DataFrame(data, columns=['Height_cm', 'Weight_kg'])

# A sample of 8 rows
print("\nSample of 8 rows : ")
print(df.sample(8))
# A summary of the data
print("\nSummary of the data : ")
print(df.describe())

print("\n - - - - - - - - - - - - - - - - ", end="\n\n")

#
# # Step 3: Handling the Missing Values
print("\nStep 3: Checking for and handling any missing values in the dataset.")

# Check for null values in the dataset
null_values = df.isnull().sum()
print("Null Values in each column:")
print(null_values)

# Check if there are any missing values
if null_values.any():
    print("\nMissing values found. Proceeding to handle them...")
    # Options for handling missing values:
    # 1. Drop rows with missing values: df = df.dropna()
    # 2. Fill missing values with the mean: df = df.fillna(df.mean())
else:
    print("\nNo missing values detected. Proceeding to the next step.")

# #
# Since there are no null values, we can proceed with the data.
# However, if there were null values, we would have to either drop the rows or fill them with the mean value 
# or any other value that would be appropriate.
# Either of the following two lines can be used to do so.
# For droping the null value rows - df = df.dropna()
# For filling the null values with the mean value - df = df.fillna(df.mean())
# #

print("\n - - - - - - - - - - - - - - - - ", end="\n\n")

#
# Step 4: Extracting Meaningful Insights
print("\nStep 4: Extracting meaningful insights from the data, including statistical metrics and relationships.")

# Calculating and displaying the correlation between Height and Weight
# A high correlation would indicate a linear relationship
correlation = df['Height_cm'].corr(df['Weight_kg'])
print(f"\nCorrelation between Height and Weight: {correlation:.2f}")

# Mean, Median, Mode, Min, Max, and Quartiles for Height and Weight
print("\nBasic Statistics for Height and Weight:")
print(df.describe())

# Calculating the range of height and weight
# The range gives a basic idea of the spread.
height_range = df['Height_cm'].max() - df['Height_cm'].min()
weight_range = df['Weight_kg'].max() - df['Weight_kg'].min()
print(f"\nRange of Height: {height_range:.2f} cm")
print(f"Range of Weight: {weight_range:.2f} kg")

# Calculating variance and standard deviation
# Variance and standard deviation show how far the data points tend to be from the mean, 
# with high values indicating more variability.
height_variance = df['Height_cm'].var()
weight_variance = df['Weight_kg'].var()
height_std = df['Height_cm'].std()
weight_std = df['Weight_kg'].std()
print(f"\nVariance of Height: {height_variance:.2f}")
print(f"Variance of Weight: {weight_variance:.2f}")
print(f"Standard Deviation of Height: {height_std:.2f}")
print(f"Standard Deviation of Weight: {weight_std:.2f}")

# Checking the skewness of the data
# Skewness tells us if the data is balanced (symmetric) or if it leans towards higher or lower values.
# Skewness helps in understanding the shape of the distribution: 
# Positive skew means a right skewed distribution, negative skew means left skewed
height_skewness = df['Height_cm'].skew()
weight_skewness = df['Weight_kg'].skew()
print(f"\nSkewness of Height: {height_skewness:.2f}")
print(f"Skewness of Weight: {weight_skewness:.2f}")

# Calculating the Height-to-Weight Ratio
# This ratio gives an idea of the proportionality between height and weight. 
# A consistent ratio could indicate a predictable relationship, 
# while large variations might signal that other factors affect weight besides height alone.
df['Height_to_Weight_Ratio'] = df['Height_cm'] / df['Weight_kg']
print("\nHeight-to-Weight Ratio calculated for each entry.")
print(df[['Height_cm', 'Weight_kg', 'Height_to_Weight_Ratio']].head())

print("\n - - - - - - - - - - - - - - - - ", end="\n\n")

#
# # Step 5: Data Visualization
print("\nStep 5: Visualizing data trends and patterns.")

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Histogram for Height
axs[0].hist(df['Height_cm'], bins=20, color='skyblue', edgecolor='black')
axs[0].set_title('Histogram of Height (cm)')
axs[0].set_xlabel('Height (cm)')
axs[0].set_ylabel('Frequency')
axs[0].grid(axis='y', alpha=0.75)

# Histogram for Weight
axs[1].hist(df['Weight_kg'], bins=20, color='salmon', edgecolor='black')
axs[1].set_title('Histogram of Weight (kg)')
axs[1].set_xlabel('Weight (kg)')
axs[1].set_ylabel('Frequency')
axs[1].grid(axis='y', alpha=0.75)

plt.tight_layout()
plt.show()

# Creating a scatter plot for Weight vs. Height
plt.figure(figsize=(14, 6))
plt.scatter(df['Height_cm'], df['Weight_kg'], color='purple', alpha=0.6)
plt.title('Scatter Plot of Weight vs. Height')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()

#
# # Predictions using scikit-learn
print("\nMaking predictions using a linear regression model.")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Defining the features and target variable
X = df[['Height_cm']]  # Features (Height)
y = df['Weight_kg']    # Target (Weight)

# Splitting the dataset into training and testing sets
# 80% of the data is used for training the model, while 20% is used for testing its performance
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a Linear Regression model
model = LinearRegression()

# Training the model with the training data
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model
# Mean Squared Error (MSE) measures the average squared difference between actual and predicted values
mse = mean_squared_error(y_test, y_pred)
# R-squared (R²) indicates the proportion of variance explained by the independent variable
r2 = r2_score(y_test, y_pred)

# Output of the results
print(f"\nModel Performance:")
# Lower values indicate better model performance
print(f"Mean Squared Error (MSE): {mse:.2f}")
# Values closer to 1 indicate a better fit
print(f"R-squared (R2): {r2:.2f}")

# Plotting the predictions vs actual values
plt.figure(figsize=(14, 6))
# Actual values in blue
plt.scatter(X_test, y_test, color='blue', label='Actual Weight')
# Predicted values in red
plt.scatter(X_test, y_pred, color='red', label='Predicted Weight')
plt.plot(X_test, y_pred, color='orange', linewidth=2, label='Regression Line')  # Regression line
plt.title('Actual vs Predicted Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.grid(True)
plt.show()
