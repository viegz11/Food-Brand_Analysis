import pandas as pd
import glob

# Step 1: Path to your Excel files
path = r"C:/Viegz/PowerBI/F&B/usd/*.xlsx"

# Step 2: Get all Excel files
all_files = glob.glob(path)
print("Files found:", all_files)  # Debugging

# Step 3: Combine if files exist
if all_files:
    df = pd.concat([pd.read_excel(f) for f in all_files], ignore_index=False)
    df.to_excel("Merged_usd.xlsx", index=False)
    print("✅ Combined file created: combined_reviews.xlsx")
else:
    print("⚠️ No Excel files found at the path. Check folder and extension.")
