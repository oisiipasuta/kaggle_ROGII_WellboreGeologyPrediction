from pathlib import Path
import kagglehub

COMPETITION = "rogii-wellbore-geology-prediction"
OUTPUT_DIR = "/kaggle/input/rogii-wellbore-geology-prediction"

path = kagglehub.competition_download(
    COMPETITION,
    output_dir=OUTPUT_DIR
)

print("Downloaded to:", path)

print("\n=== Files ===")
for p in Path(path).iterdir():
    print(p.name)
