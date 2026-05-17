import pandas as pd

file_path = "data/raw/Enrichment Datasets/Postal Area, Indexes, SEIFA 2021.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Table 1",
    header=None
)

print(df.head(20))