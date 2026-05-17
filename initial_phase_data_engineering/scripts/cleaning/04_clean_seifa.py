import pandas as pd

file_path = "data/raw/Enrichment Datasets/Postal Area, Indexes, SEIFA 2021.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Table 1",
    header=5
)

# Clean column names
df.columns = (
    df.columns
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

print(df.columns.tolist())