import pandas as pd

file_path = "data/raw/Enrichment Datasets/Population estimates and components by LGA, 2024 to 2025.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Table 1",
    header=None
)

print(df.head(20))