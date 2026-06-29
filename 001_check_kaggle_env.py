from pathlib import Path
import pandas as pd
import numpy as np
import sklearn
import lightgbm as lgb

print("=== Library Check ===")
print("pandas:", pd.__version__)
print("numpy:", np.__version__)
print("sklearn:", sklearn.__version__)
print("lightgbm:", lgb.__version__)

print("\n=== Directory Check ===")
print("/kaggle/working exists:", Path("/kaggle/working").exists())
print("/kaggle/input exists:", Path("/kaggle/input").exists())

print("\n=== /kaggle/input files ===")
input_dir = Path("/kaggle/input")
for p in input_dir.rglob("*"):
    print(p)
