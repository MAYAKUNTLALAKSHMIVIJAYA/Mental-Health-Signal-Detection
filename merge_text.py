# merge_goemotions.py
import pandas as pd
import os

# Path to the folder containing the 3 CSVs
text_data_path = "data/text_data"

# List all CSV files in that folder
csv_files = ["goemotions_1.csv", "goemotions_2.csv", "goemotions_3.csv"]

# Read and merge all CSVs
df_list = []
for file in csv_files:
    file_path = os.path.join(text_data_path, file)
    df = pd.read_csv(file_path)
    df_list.append(df)

# Concatenate all dataframes
combined_df = pd.concat(df_list, ignore_index=True)

# Save to a new CSV
output_path = os.path.join(text_data_path, "combined_goemotions.csv")
combined_df.to_csv(output_path, index=False)

print(f"Merged CSV saved to: {output_path}")