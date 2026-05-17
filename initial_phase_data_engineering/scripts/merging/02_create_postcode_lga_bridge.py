import pandas as pd
import os

# Load bridge datasets
poa = pd.read_excel(
    "data/raw/Geography Bridge Datasets/POA_2021_AUST.xlsx"
)

lga = pd.read_excel(
    "data/raw/Geography Bridge Datasets/LGA_2025_AUST.xlsx"
)

print("\nPOA Shape:", poa.shape)
print("LGA Shape:", lga.shape)

# Standardise columns
poa.columns = (
    poa.columns
    .str.lower()
    .str.strip()
)

lga.columns = (
    lga.columns
    .str.lower()
    .str.strip()
)

# Merge through mesh block
bridge = poa.merge(
    lga,
    on="mb_code_2021",
    how="inner"
)

print("\nMerged Shape:", bridge.shape)

# Keep only useful columns
bridge = bridge[
    [
        "poa_code_2021",
        "poa_name_2021",
        "lga_code_2025",
        "lga_name_2025",
        "state_name_2021"
    ]
]

# Rename cleanly
bridge = bridge.rename(columns={
    "poa_code_2021": "postcode",
    "poa_name_2021": "postcode_name",
    "lga_code_2025": "lga_code",
    "lga_name_2025": "lga_name",
    "state_name_2021": "state_name"
})

# Clean postcode
bridge["postcode"] = (
    bridge["postcode"]
    .astype(str)
    .str.strip()
    .str.zfill(4)
)

# Remove duplicates
bridge = bridge.drop_duplicates()

# Remove nulls
bridge = bridge.dropna()

print("\nFinal Shape:", bridge.shape)

print("\nPreview:")
print(bridge.head())

# Save
os.makedirs("data/final_tableau", exist_ok=True)

bridge.to_csv(
    "data/final_tableau/postcode_lga_bridge.csv",
    index=False
)

print("\nPostcode-LGA bridge created successfully.")