import json
import sys
import os
from collections import defaultdict
import re

# Define the function to convert the input JSON to the desired output JSON structure
def convert_json(input_data):
    output_json = {
        "projections": []
    }

    def parse_region_tracer(entry):
        match = re.match(r'[A-Z]+\d{6}-\d{2}[A-Z]-([\w]+)\/\d-([\w]+)', entry)
        if match:
            return match.groups()
        return entry, entry

    def process_projections(data, label, class_name):
        region_count = defaultdict(int)
        regions = []

        for entry in data:
            region, tracer = parse_region_tracer(entry)

            # Replace specific keys with different aliases
            if region == "DP":
                region = "DPs"
            elif region == "DP_deep":
                region = "DPd"

            region_count[region] += 1
            region_label = f"{region}{region_count[region]}"
            regions.append({"class": entry, "label": region_label})

        return {
            "label": label,
            "class": class_name,
            "regions": regions
        }

    # Convert anterograde data
    anterograde_projection = process_projections(input_data["anterograde"], "Anterograde", "anterograde")
    output_json["projections"].append(anterograde_projection)

    # Convert retrograde data
    retrograde_projection = process_projections(input_data["retrograde"], "Retrograde", "retrograde")
    output_json["projections"].append(retrograde_projection)

    return output_json

# Check if the input and output folder paths are provided
if len(sys.argv) < 3:
    print("Usage: python script.py <input_json_file> <output_folder>")
    sys.exit(1)

# Read the input file path and output folder path from the command line
input_file_path = sys.argv[1]
output_folder_path = sys.argv[2]

# Ensure the output folder exists, create it if necessary
os.makedirs(output_folder_path, exist_ok=True)

# Read the input JSON from the file
with open(input_file_path, 'r') as input_file:
    input_json = json.load(input_file)

# Convert the input JSON
output_json = convert_json(input_json)

# Define the output file path
output_file_path = os.path.join(output_folder_path, 'imageMenu.json')

# Write the output JSON to a file
with open(output_file_path, 'w') as output_file:
    json.dump(output_json, output_file, indent=4)

print(f'Converted JSON has been written to {output_file_path}')
