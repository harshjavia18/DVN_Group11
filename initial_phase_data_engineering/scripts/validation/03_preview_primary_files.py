import pandas as pd

files = {
    "refunds": {
        "path": "data/raw/Primary Datasets/rentalbond_refunds_year_2025.xlsx",
        "sheet": "Year 2025 RBS Refunds"
    },
    "bonds_held": {
        "path": "data/raw/Primary Datasets/rentalbond_bondsheld_as_at_december_2025.xlsx",
        "sheet": "Residential Bond Held"
    }
}

for name, info in files.items():
    print("\n" + "=" * 80)
    print(name.upper())
    print("=" * 80)

    df = pd.read_excel(
        info["path"],
        sheet_name=info["sheet"],
        header=None
    )

    print(df.head(20))