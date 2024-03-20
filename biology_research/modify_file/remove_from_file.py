import json
import msvcrt


def check_10_records(data, total_records, num_records_analyzed, total_alive):
    list_of_delete_index = []
    for i in range(num_records_analyzed, num_records_analyzed + 10):
        if data[i]['deaths'] > total_alive:
            list_of_delete_index.append(i)
        else:
            total_alive += data[i]['births']
    return list_of_delete_index


def read_and_write_json_file(filename):
    # Open the JSON file in read/write mode
    with open(filename, 'r+') as file:
        # Acquire an exclusive lock for both reading and writing
        msvcrt.locking(file.fileno(), msvcrt.LK_LOCK)

        # Read the JSON data
        file.seek(0)  # Move the file pointer to the beginning
        json_data = json.load(file)

        # Modify the JSON data (example)
        json_data['new_key'] = 'new_value'

        # Write the modified JSON data back to the file
        file.seek(0)  # Move the file pointer to the beginning
        json.dump(json_data, file, indent=4)
        file.truncate()

        # Release the lock on the file
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK)


# Example usage:
filename = 'data.json'
read_and_write_json_file(filename)
