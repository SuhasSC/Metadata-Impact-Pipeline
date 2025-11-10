import pandas as pd

# Load raw metadata
df = pd.read_csv("data/raw_documents.csv")

# Example metadata cleaning (customize as needed)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
df.dropna(how="all", inplace=True)  # remove rows with all NaNs
df.drop_duplicates(inplace=True)    # remove duplicate rows

# Save cleaned data with utf-8 encoding
df.to_csv("data/clean_documents.csv", index=False, encoding="utf-8")

# Use plain text to avoid UnicodeEncodeError in Windows console
print("Cleaned metadata saved to data/clean_documents.csv")
