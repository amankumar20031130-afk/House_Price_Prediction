import csv
import json

input_file = "housing.csv"
output_file = "mapdata.json"

data = []

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        clean_row = {}
        
        for key, value in row.items():
            # If empty -> set to None (JSON null)
            if value == "" or value is None:
                clean_row[key] = None
            else:
                # Try converting numbers safely
                try:
                    num = float(value)
                    # Convert integers properly (avoid .0)
                    if num.is_integer():
                        num = int(num)
                    clean_row[key] = num
                except:
                    # Keep strings (like ocean_proximity)
                    clean_row[key] = value
        
        data.append(clean_row)

# Save JSON
with open(output_file, "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=2)

print("✔ Conversion complete: mapdata.json created successfully.")
