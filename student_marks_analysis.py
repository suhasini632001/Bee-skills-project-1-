import pandas as pd
import numpy as np

# Step 1: Read the dataset
data = pd.read_csv("student_marks.csv")

# Step 2: Display first 5 records
print("First 5 Records:")
print(data.head())

# Step 3: Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 4: Fill missing numerical values with mean
numeric_columns = data.select_dtypes(include=np.number).columns

for column in numeric_columns:
    data[column] = data[column].fillna(data[column].mean())

# Step 5: Calculate average marks
print("\nAverage Scores:")
print(data[numeric_columns].mean())

# Step 6: Calculate maximum marks
print("\nMaximum Scores:")
print(data[numeric_columns].max())

# Step 7: Calculate minimum marks
print("\nMinimum Scores:")
print(data[numeric_columns].min())

# Step 8: Display cleaned data
print("\nCleaned Dataset:")
print(data.head())

# Step 9: Save cleaned dataset
data.to_csv("cleaned_student_marks.csv", index=False)

print("\nAnalysis completed successfully!")