import pandas as pd

# Dataset 1: Students info
students = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

# Dataset 2: Students scores
scores = pd.DataFrame({
    'ID': [1, 2, 3],
    'Math': [85, 90, 95],
    'Science': [88, 92, 97]
})

print("Dataset 1:\n", students)
print("\nDataset 2:\n", scores)

# Data Integration: Merge datasets on 'ID'
merged_data = pd.merge(students, scores, on='ID')
print("\nIntegrated Dataset:\n", merged_data)

