from pathlib import Path
import pandas as pd

DATA_DIR = Path("/kaggle/input/rogii-wellbore-geology-prediction")

csv_files = sorted(DATA_DIR.rglob("*.csv"))

print("=== CSV FILES ===")
for path in csv_files:
    print(path)

for path in csv_files:
    print("\n" + "=" * 80)
    print("FILE:", path.name)

    df = pd.read_csv(path)

    print("\n--- shape ---")
    print(df.shape)

    print("\n--- columns ---")
    for i, col in enumerate(df.columns):
        print(f"{i:03d}: {col}")

    print("\n--- dtypes ---")
    print(df.dtypes)

    print("\n--- missing values top 30 ---")
    print(df.isna().sum().sort_values(ascending=False).head(30))

    print("\n--- head ---")
    print(df.head())

    print("\n--- numeric describe ---")
    print(df.describe(include="number").T.head(50))
