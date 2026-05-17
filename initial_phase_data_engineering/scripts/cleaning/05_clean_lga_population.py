import pandas as pd
import os

file_path = "data/raw/Enrichment Datasets/Population estimates and components by LGA, 2024 to 2025.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Table 1",
    header=5
)

df.columns = (
    df.columns
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace(" ", "_", regex=False)
)

# Rename actual columns
df = df.rename(columns={
    "lga_code": "lga_code",
    "lga_name": "lga_name",
    "no.": "population_2024",
    "no..1": "births",
    "no..2": "deaths",
    "no..3": "net_internal_migration",
    "no..4": "net_overseas_migration",
    "no..5": "population_2025",
    "km2": "area_sqkm",
    "persons/km2": "population_density_2025"
})

keep_cols = [
    "lga_code",
    "lga_name",
    "population_2024",
    "births",
    "deaths",
    "net_internal_migration",
    "net_overseas_migration",
    "population_2025",
    "area_sqkm",
    "population_density_2025"
]

df = df[keep_cols]

df = df.dropna(subset=["lga_code"])

df["lga_code"] = df["lga_code"].astype(str).str.strip()
df["lga_name"] = df["lga_name"].astype(str).str.strip()

for col in df.columns:
    if col not in ["lga_code", "lga_name"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

df = df.drop_duplicates(subset=["lga_code"])
df = df.fillna(0)

os.makedirs("data/final_tableau", exist_ok=True)

df.to_csv(
    "data/final_tableau/dashboard_lga_population.csv",
    index=False
)

print("\nFinal Shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())
print("\nPreview:")
print(df.head())
print("\nLGA population dataset created successfully.")