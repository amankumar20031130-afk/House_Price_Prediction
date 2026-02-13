# generate_mapdata.py
import pandas as pd
import json
import os

# Create static directory if it doesn't exist
os.makedirs("static", exist_ok=True)

# Load dataset
df = pd.read_csv("housing.csv")

# OPTIONAL: reduce size for faster frontend rendering
sample_size = 3000
if sample_size and len(df) > sample_size:
    df_small = df.sample(sample_size, random_state=42).reset_index(drop=True)
else:
    df_small = df.copy()

# Keep only fields we need
cols = [
    "longitude", "latitude", "housing_median_age", "total_rooms",
    "total_bedrooms", "population", "households", "median_income", "ocean_proximity",
    "median_house_value"
]

# Clean data: drop rows with ANY NaN values to ensure valid JSON
df_small = df_small[cols].dropna().reset_index(drop=True)

# convert to list of dicts
records = df_small.to_dict(orient="records")

# write JSON to static folder
output_path = os.path.join("static", "mapdata.json")
with open(output_path, "w") as f:
    # ensure no NaN/inf values are written as bare tokens
    json.dump(records, f)

print(f"mapdata.json created in 'static/' with {len(records)} clean records.")

