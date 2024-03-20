
import json
import os

def load_json_files(directory):
    """Load data from a set of JSON files in the specified directory."""
    all_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                try:
                    data = json.load(file)
                    all_data.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON from file '{filename}': {e}")
    return all_data


def merge_data(data,key):
    merged_data = []
    for data_list in data:
        merged_data = merged_data + data_list[key]
    return merged_data

