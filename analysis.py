# Import required libraries for data handling and text processing
import pandas as pd
import re

# Load dataset from Excel file
file_path = "Dataset for Data Analytics.xlsx"
df = pd.read_excel(file_path)

# Keep a backup of original dataset for comparison
raw_df = df.copy()

# -------------------------------
# BASIC DATA OVERVIEW
# -------------------------------
print(df.head())              # view sample records
print(df.shape)              # dataset size (rows, columns)
print(df.columns)            # column names
print(df.info())             # data types and null info
print(df.isnull().sum())     # missing values per column
print(df.duplicated().sum()) # count of duplicate rows

# Handle missing values in CouponCode column
df['CouponCode'] = df['CouponCode'].fillna("No Coupon")

# Confirm missing values handled
print(df['CouponCode'].isnull().sum())

# -------------------------------
# STANDARDIZE COLUMN NAMES
# -------------------------------
# Convert column names into snake_case format for consistency
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace(r"(?<=[a-z0-9])(?=[A-Z])", "_", regex=True)
    .str.lower()
)

# -------------------------------
# TOTAL PRICE VALIDATION
# -------------------------------

# Recalculate expected total price using business rule
df["calculated_total"] = df["quantity"] * df["unit_price"]

# Identify differences between actual and calculated values
df["mismatch"] = (df["total_price"] - df["calculated_total"]).abs()

# Display rows where mismatch exists (if any)
print(df[df["mismatch"] > 0.01])

# Correct total price using calculated values
df["total_price"] = df["calculated_total"]

# Remove temporary validation columns
df.drop(["calculated_total", "mismatch"], axis=1, inplace=True)

# Create a structured log of all data cleaning steps performed
log_data = [
    ["Step 1", "Missing values handled", "CouponCode filled with 'No Coupon'"],
    ["Step 2", "Column standardization", "Converted column names to snake_case format"],
    ["Step 3", "TotalPrice validation", "Recalculated total_price using quantity × unit_price and fixed mismatches"],
    ["Step 4", "Duplicate check", "Checked and verified duplicate rows"],
    ["Step 5", "Final export", "Saved cleaned dataset with log sheet in Excel"]
]

log_df = pd.DataFrame(log_data, columns=["Step", "Action", "Result"])

# Confirm validation completion
print("TotalPrice validation completed successfully.")

# -------------------------------
# COLUMN CHECK AFTER CLEANING
# -------------------------------
print(df.columns.tolist())
print(df.columns)

# Save cleaned dataset to Excel file
with pd.ExcelWriter("cleaned_dataset.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned_Data", index=False)
    log_df.to_excel(writer, sheet_name="Cleaning_Log", index=False)
print("Cleaned file saved successfully!")

# -------------------------------
# FINAL DATA VALIDATION
# -------------------------------
print("\nFINAL DATA VALIDATION AFTER CLEANING")

print("\nMissing Values (After Cleaning):")
print(df.isnull().sum())

print("\nDuplicate Rows (After Cleaning):")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

# -------------------------------
# DATA QUALITY METRICS SUMMARY
# -------------------------------
print("\nDATA QUALITY METRICS")

metrics = {
    "Rows Before Cleaning": len(raw_df),
    "Rows After Cleaning": len(df),
    "Total Missing Values": df.isnull().sum().sum(),
    "Duplicate Rows": df.duplicated().sum()
}

# Display summary metrics
for key, value in metrics.items():
    print(f"{key}: {value}")