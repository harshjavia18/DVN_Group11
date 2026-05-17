import pandas as pd

file_path = "data/raw/Primary Datasets/rentalbond_lodgements_year_2025.xlsx"

# Read WITHOUT headers
df = pd.read_excel(
    file_path,
    sheet_name="Year 2025 Rental Bond Lodgments",
    header=None
)

# Show first 20 rows
print(df.head(20))