import pandas as pd
import os

lodgements = pd.read_csv("data/cleaned/lodgements_cleaned.csv")
refunds = pd.read_csv("data/cleaned/refunds_cleaned.csv")
bonds = pd.read_csv("data/cleaned/bonds_held_cleaned.csv")
seifa = pd.read_csv("data/cleaned/seifa_cleaned.csv")

# Make postcode consistent
for df in [lodgements, refunds, bonds, seifa]:
    df["postcode"] = df["postcode"].astype(str).str.strip().str.zfill(4)

# Lodgement metrics
lodgement_summary = (
    lodgements.groupby("postcode")
    .agg(
        total_lodgements=("postcode", "count"),
        avg_weekly_rent=("weekly_rent", "mean"),
        median_weekly_rent=("weekly_rent", "median")
    )
    .reset_index()
)

# Refund metrics
refund_summary = (
    refunds.groupby("postcode")
    .agg(
        total_refunds=("postcode", "count"),
        avg_days_bond_held=("days_bond_held", "mean"),
        median_days_bond_held=("days_bond_held", "median"),
        avg_payment_to_tenant=("payment_to_tenant", "mean")
    )
    .reset_index()
)

# Merge
dashboard = (
    lodgement_summary
    .merge(refund_summary, on="postcode", how="left")
    .merge(bonds, on="postcode", how="left")
    .merge(seifa, on="postcode", how="left")
)

# Fill count fields with 0
count_cols = ["total_refunds", "bonds_held"]
for col in count_cols:
    dashboard[col] = dashboard[col].fillna(0)

# Fill numeric missing values with median
for col in dashboard.columns:
    if col != "postcode":
        dashboard[col] = pd.to_numeric(dashboard[col], errors="coerce")
        dashboard[col] = dashboard[col].fillna(dashboard[col].median())

# Add useful dashboard metrics
dashboard["refund_to_lodgement_ratio"] = (
    dashboard["total_refunds"] / dashboard["total_lodgements"]
).round(3)

dashboard["rent_pressure_score"] = (
    dashboard["median_weekly_rent"] / dashboard["seifa_disadvantage_score"]
).round(3)

# Final cleanup
dashboard = dashboard.drop_duplicates(subset=["postcode"])
dashboard = dashboard.fillna(0)

# Round numbers
numeric_cols = dashboard.select_dtypes(include="number").columns
dashboard[numeric_cols] = dashboard[numeric_cols].round(2)

os.makedirs("data/final_tableau", exist_ok=True)

dashboard.to_csv(
    "data/final_tableau/dashboard_postcode_rental.csv",
    index=False
)

print("\nFinal Shape:")
print(dashboard.shape)

print("\nColumns:")
print(dashboard.columns.tolist())

print("\nMissing values:")
print(dashboard.isna().sum())

print("\nPreview:")
print(dashboard.head())

print("\nFinal postcode rental dashboard dataset created successfully.")