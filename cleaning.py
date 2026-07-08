# ==========================================
# Netflix Dataset Cleaning using Pandas
# ==========================================

import pandas as pd

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------
df = pd.read_csv("netflix_titles.csv")

print("=" * 50)
print("First 5 Rows")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("Dataset Information")
print("=" * 50)
print(df.info())

print("\nDataset Shape:", df.shape)

# ------------------------------------------
# 2. Check Missing Values
# ------------------------------------------
print("\n" + "=" * 50)
print("Missing Values Before Cleaning")
print("=" * 50)
print(df.isnull().sum())

# ------------------------------------------
# 3. Remove Duplicate Records
# ------------------------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df.drop_duplicates(inplace=True)

# ------------------------------------------
# 4. Remove Leading & Trailing Spaces
# ------------------------------------------
string_columns = [
    "title",
    "director",
    "cast",
    "country",
    "rating",
    "duration",
    "listed_in",
    "description",
    "date_added"
]

for col in string_columns:
    df[col] = df[col].astype("string").str.strip()

# ------------------------------------------
# 5. Fill Missing Values
# ------------------------------------------
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")

# Fill rating with most frequent value
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

# ------------------------------------------
# 6. Convert Date Column
# ------------------------------------------
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Fill missing dates with most common date
df["date_added"] = df["date_added"].fillna(
    df["date_added"].mode()[0]
)

# ------------------------------------------
# 7. Check Data Types
# ------------------------------------------
print("\n" + "=" * 50)
print("Data Types")
print("=" * 50)
print(df.dtypes)

# ------------------------------------------
# 8. Verify Missing Values
# ------------------------------------------
print("\n" + "=" * 50)
print("Missing Values After Cleaning")
print("=" * 50)
print(df.isnull().sum())

# ------------------------------------------
# 9. Save Cleaned Dataset
# ------------------------------------------
output_file = "netflix_titles_cleaned.csv"
df.to_csv(output_file, index=False)

print("\n" + "=" * 50)
print("Dataset Cleaned Successfully!")
print(f"Cleaned file saved as: {output_file}")
print("=" * 50)