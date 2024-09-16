#!/bin/bash



#!/bin/bash

# Define the input directory where the FASTA files are located
input_dir="/Users/u0107886/Library/CloudStorage/OneDrive-KULeuven/C1 Iron/Proteomics/down_fasta"
# Define the directory where you want to store the results
output_base_dir="/Users/u0107886/Library/CloudStorage/OneDrive-KULeuven/C1 Iron/Proteomics/UP/DOWNResults"
# Define the Biolib results directory
biolib_results_dir="/Users/u0107886/biolib_results"


# Make sure the Results directory exists
mkdir -p "$output_base_dir"

# Loop through all .fasta files in the input directory
for fasta_file in "$input_dir"/*.fasta; do
  # Get the filename without the path
  filename=$(basename -- "$fasta_file")
  
  # Extract the prefix of the filename (i.e., everything before the ".fasta")
  prefix="${filename%.fasta}"

  # Create a subdirectory in the Results folder named after the prefix
  output_dir="$output_base_dir/$prefix"
  mkdir -p "$output_dir"

  # Run the biolib command (results will be stored in default location)
  biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "$fasta_file"

  # Find the results and move them to the desired output directory
  # Assuming the results are stored in the current working directory, you may need to modify this depending on biolib's behavior
  mv "$biolib_results_dir"/* "$output_dir"

  echo "Processed $fasta_file, results moved to $output_dir"
done
