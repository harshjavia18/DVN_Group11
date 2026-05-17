import pandas as pd
import os

file_path = "data/raw/Primary Datasets/rentalbond_refunds_year_2025.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Year 2025 RBS Refunds",
    header=2
)

print("\nOriginal Shape:")
print(df.shape)

# Standardize columns
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

print("\nColumns:")
print(df.columns.tolist())

# Remove rows with missing postcode
df = df.dropna(subset=["postcode"])

# Convert postcode
df["postcode"] = df["postcode"].astype(str)

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Shape:")
print(df.shape)

print("\nPreview:")
print(df.head())

# Save
os.makedirs("data/cleaned", exist_ok=True)

df.to_csv(
    "data/cleaned/refunds_cleaned.csv",
    index=False
)

print("\nRefunds cleaned successfully.")