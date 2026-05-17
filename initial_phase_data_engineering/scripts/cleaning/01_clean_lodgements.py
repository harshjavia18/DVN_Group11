import pandas as pd

# File path
file_path = "data/raw/Primary Datasets/rentalbond_lodgements_year_2025.xlsx"

# Read actual data
df = pd.read_excel(
    file_path,
    sheet_name="Year 2025 Rental Bond Lodgments",
    header=2
)

print("\nOriginal Shape:")
print(df.shape)

# Standardize column names
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

# Rename important columns
df = df.rename(columns={
    "lodgement_date": "lodgement_date",
    "postcode": "postcode",
    "dwelling_type": "dwelling_type",
    "bedrooms": "bedrooms",
    "weekly_rent": "weekly_rent"
})

# Convert date
df["lodgement_date"] = pd.to_datetime(
    df["lodgement_date"],
    errors="coerce"
)

# Remove rows with missing postcode or rent
df = df.dropna(subset=["postcode", "weekly_rent"])

# Convert data types
df["postcode"] = df["postcode"].astype(str)

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nPreview:")
print(df.head())

# Save cleaned dataset
output_path = "data/cleaned"

import os
os.makedirs(output_path, exist_ok=True)

df.to_csv(
    f"{output_path}/lodgements_cleaned.csv",
    index=False
)

print("\nCleaned file saved successfully.")