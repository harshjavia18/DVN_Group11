import pandas as pd
import os

file_path = "data/raw/Primary Datasets/rentalbond_bondsheld_as_at_december_2025.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Residential Bond Held",
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

# Rename columns
df = df.rename(columns={
    "postcode": "postcode",
    "bonds_held": "bonds_held"
})

# Remove nulls
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
    "data/cleaned/bonds_held_cleaned.csv",
    index=False
)

print("\nSaved successfully.")