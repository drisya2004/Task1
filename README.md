# DecodeLabs-Internship
Projects completed during DecodeLabs Data Analytics Internship
Data Cleaning
📌 Project Overview

This project implements a complete data cleaning, validation, and quality assessment pipeline using Python (pandas).

The script:

Loads raw data from an Excel file
Performs structured cleaning and validation
Fixes inconsistencies using business rules
Logs every cleaning step
Exports a cleaned dataset + cleaning log into a new Excel file

📂 Repository Structure

├── Dataset for Data Analytics.xlsx   # Raw input dataset
├── cleaned_dataset.xlsx              # Cleaned output with log
├── data_cleaning.py                  # Python cleaning script
├── README.md

📄 Input Dataset
File: Dataset for Data Analytics.xlsx
Format: Excel (.xlsx)
Status: Raw / Uncleaned

A backup copy of the raw dataset is preserved in memory for comparison.

🔍 Data Cleaning Workflow
1️⃣ Basic Data Overview

The script performs an initial inspection:

Sample records (head())
Dataset shape (rows × columns)
Column names
Data types & null values
Missing value counts
Duplicate row count
2️⃣ Missing Value Handling
Column affected: CouponCode

Action:
Missing values are replaced with:

"No Coupon"

3️⃣ Column Name Standardization

All column names are converted to snake_case for consistency:

Trims whitespace
Replaces spaces with underscores
Splits camelCase
Converts to lowercase

Example:

TotalPrice → total_price
Unit Price → unit_price
4️⃣ Business Rule Validation (Total Price)

A validation rule is applied:

total_price = quantity × unit_price

Steps:
Recalculate expected total
Detect mismatches
Correct incorrect total_price values
Remove temporary validation columns

This ensures financial accuracy in the dataset.

5️⃣ Duplicate Verification
Duplicate rows are checked and reported
No automatic deletion unless required
6️⃣ Cleaning Log Creation

All cleaning steps are documented in a structured log:
| Step   | Action                 | Result               |
| ------ | ---------------------- | -------------------- |
| Step 1 | Missing values handled | CouponCode filled    |
| Step 2 | Column standardization | snake_case applied   |
| Step 3 | Total price validation | Corrected mismatches |
| Step 4 | Duplicate check        | Verified             |
| Step 5 | Final export           | Cleaned file saved   |

This log is exported as a separate Excel sheet.

📤 Output Files
✅ cleaned_dataset.xlsx

Contains two sheets:

Cleaned_Data
Fully cleaned dataset
Validated prices
Standardized columns
Cleaning_Log
Step-by-step record of cleaning actions
📊 Final Data Validation
After cleaning, the script verifies:

Missing values → 0
Duplicate rows
Correct data types
Row count consistency

📈 Data Quality Metrics
Rows Before Cleaning
Rows After Cleaning
Total Missing Values
Duplicate Rows

🛠️ Technologies Used
Python 
pandas
Regular Expressions (re)
Excel (.xlsx)

▶️ How to Run
pip install pandas openpyxl
python analysis.py

Ensure the input Excel file is in the same directory.

🎯 Use Cases
Data analytics projects
Academic mini / final-year projects
Business data validation
Financial transaction cleaning
Data quality auditing

Author:
Drisya M
