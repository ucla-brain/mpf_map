import json
from collections import defaultdict

# Function to read JSON file and return data
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to extract key value pairs and handle collisions
def extract_key_value_pairs(data):
    roi_counter = defaultdict(int)  # Dictionary to count occurrences of each roi
    key_value_pairs = {}

    for key in data.keys():
        parts = key.split('-')
        if len(parts) >= 4:
            print(parts)
            roi = parts[2].split('/')[0]  # Split by '/' and take the second part for tracer            
            tracer = parts[3]

            # Handle collisions for roi
            if roi in key_value_pairs:
                roi_counter[roi] += 1
                roi = f"{roi}{roi_counter[roi]}"
            else:
                roi_counter[roi] = 0

            key_value_pairs[roi] = tracer

    return key_value_pairs

# Function to print regions in the specified format
def print_regions(key_value_pairs):
    regions = {"regions": []}

    for key, value in key_value_pairs.items():
        print(value)
        regions["regions"].append({
            "region": [{
                "class": key.lower(),
                "label": key
            }]
        })

    # Convert to JSON string and format as needed
    json_str = json.dumps(regions, separators=(',', ':'), indent=None)
    
    # Replace double quotes around values with single quotes
    formatted_str = json_str.replace('"class":', 'class:').replace('"label":', 'label:').replace('"region":', 'region:').replace('"regions":', 'regions:').replace('\"', '\'')

    print(formatted_str)


# Main function to execute the steps
def main(json_file_path):
    data = read_json(json_file_path)
    key_value_pairs = extract_key_value_pairs(data)
    return key_value_pairs

# Example usage
if __name__ == "__main__":
    json_file_path = "/Users/seitayamashita/Documents/git_next/mpf_map/static/images/images.json"  # Replace with your JSON file path
    key_value_pairs = main(json_file_path)
    # print(key_value_pairs)
    print_regions(key_value_pairs)

