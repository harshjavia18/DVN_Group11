import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")

excel_files = list(RAW_DIR.rglob("*.xlsx"))

print(f"\nTotal Excel files found: {len(excel_files)}")

for file in excel_files:

    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)

    try:
        xls = pd.ExcelFile(file)

        print("\nSHEETS:")
        print(xls.sheet_names)

        for sheet in xls.sheet_names:

            df = pd.read_excel(
                file,
                sheet_name=sheet,
                nrows=5
            )

            print(f"\n--- SHEET: {sheet} ---")
            print("Shape Preview:", df.shape)

            print("\nColumns:")
            print(df.columns.tolist())

    except Exception as e:
        print(f"ERROR: {e}")