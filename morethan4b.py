#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:15:15 2024

@author: u0107886
"""

import os
import re
import pandas as pd

# Directory containing the subfolders
base_dir = '/Users/u0107886/Library/CloudStorage/OneDrive-KULeuven/C1 Iron/Proteomics/UP/DOWNResults'


# Output list for storing results
data = []

# Loop through the subfolders and files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)

            # Initialize variables for each file
            protein_name = None
            tmrs_count = None

            # Open and read the .md file
            with open(file_path, 'r') as f:
                lines = f.readlines()

                # Extract protein name and TMR count
                for line in lines:
                    if line.startswith(">"):
                        # Extract the protein name from the header
                        protein_name = line.split()[0].replace(">", "")

                    if "Number of predicted TMRs" in line:
                        # Use a stricter regex to ensure we are only capturing the correct number
                        match = re.search(r'Number of predicted TMRs:\s*(\d+)', line)
                        if match:
                            tmrs_count = int(match.group(1))
                            break  # Stop once we find the TMR count

            # If we found the TMR count and it's more than 4, save the result
            if tmrs_count and tmrs_count > 4:
                data.append([protein_name, tmrs_count, file_path])

# Create a DataFrame to store the results
df = pd.DataFrame(data, columns=['Protein Name', 'Number of predicted TMRs', 'File Path'])

# Save the DataFrame to an Excel file
output_file = 'proteins_down_with_more_than_4_TMRs.xlsx'
df.to_excel(output_file, index=False)

print(f"Extraction complete! Results saved in {output_file}.")
