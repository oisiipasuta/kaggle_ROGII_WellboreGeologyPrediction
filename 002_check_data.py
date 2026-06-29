from pathlib import Path
import pandas as pd

DATA_DIR = Path("/kaggle/input/rogii-wellbore-geology-prediction")

print("=== DATA DIR ===")
print(DATA_DIR)
print("exists:", DATA_DIR.exists())

print("\n=== Files ===")
files = list(DATA_DIR.rglob("*"))
for f in files:
    print(f)

print("\n=== CSV Preview ===")
csv_files = list(DATA_DIR.rglob("*.csv"))

if len(csv_files) == 0:
    print("CSV file not found.")
else:
    for csv_path in csv_files:
        print("\n--------------------")
        print("file:", csv_path.name)

        df = pd.read_csv(csv_path)
        print("shape:", df.shape)
        print("columns:")
        print(df.columns.tolist())
        print("head:")
        print(df.head())
