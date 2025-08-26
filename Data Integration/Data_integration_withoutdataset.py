import pandas as pd

# Load iris.csv
df = pd.read_csv("iris.csv")

print("Original Iris Dataset:\n", df.head())

# Example: Split features into two separate datasets to simulate integration
features1 = df[['sepal_length', 'sepal_width']]
features2 = df[['petal_length', 'petal_width', 'species']]

# Integrate (merge) back using index
integrated_df = pd.concat([features1, features2], axis=1)
print("\nIntegrated Iris Dataset:\n", integrated_df.head())