import json
import msvcrt


def check_10_records(data, num_records_analyzed, total_alive_rabbits):
    """Checks every 10 records if the number of deaths in a record is bigger than the
       total number of living rabbits then deletes the record and ignore it in the analysis
       and updates the total number of alive rabbits
       parameters: (list of dictionaries ) data of records,
       (int) num_records_analyzed
       (int) total_alive_rabbits since last analyzed
       returns: list:  indexes_to_delete
     """
    list_indexes_to_delete = []

    for i in range(num_records_analyzed, num_records_analyzed + 10):
        _, deaths_births = next(iter(data[i].items()))
        if deaths_births[0] > total_alive_rabbits:
            list_indexes_to_delete.append(i)
        else:
            total_alive_rabbits += deaths_births[1] - deaths_births[0]
    return list_indexes_to_delete

def read_and_remove_from_json_file(filename, num_records_analyzed, total_alive_rabbits):
    try:
        with open(filename, 'r+') as file:
            # Acquire an exclusive lock for both reading and writing
            msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 0)

            try:
                # Read the JSON data
                file.seek(0)  # Move the file pointer to the beginning
                json_data = json.load(file)

                indexes_to_remove = check_10_records(json_data, num_records_analyzed, total_alive_rabbits)

                for index in indexes_to_remove:
                    json_data.pop(index)

                # Write the modified JSON data back to the file
                file.seek(0)  # Move the file pointer to the beginning
                json.dump(json_data, file, indent=4)
                file.truncate()
            finally:
                # Release the lock on the file before the file is closed
                msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 0)
    except PermissionError:
        print("Permission denied. Please check file permissions or run the script with appropriate privileges.")


