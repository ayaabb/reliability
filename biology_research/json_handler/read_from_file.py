import json
import msvcrt
import os
import random
import time

failure_probability = 0
delay = 1
max_retries = 3


def read_json_data(file_path):
    retry_count = 0
    global delay

    global failure_probability
    while retry_count < max_retries:
        try:
            if random.random() < failure_probability:
                # Raise a random exception
                random_exception = random.choice([
                    FileNotFoundError,
                    PermissionError,
                    IsADirectoryError,
                    FileExistsError,
                    NotADirectoryError,
                    IOError
                ])
                raise random_exception("Random exception raised")
            else:
                with open(file_path, 'r') as file:
                    # Acquire a shared lock for reading
                    # msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)

                    # Read the JSON data
                    file.seek(0)  # Move the file pointer to the beginning
                    json_data = json.load(file)

                if failure_probability < 1.0:  # Cap the failure probability at 100%
                    failure_probability += 0.05  # Increase failure probability
                print('read operation-failure_probability after: ', failure_probability)
                return json_data
        except FileNotFoundError as e:
            # Perform file creation silently
            print(f"FileExistsError occurred: read operation - {e}.")
            failure_probability = 0  # Reset failure probability upon failure
            if not os.path.isfile(file_path):
                file_path = input("This is not path, insert the correct path :")
                print("Error fixed , Retrying...")
            else:
                print("File already exists, Retrying...")
            retry_count += 1

        except FileExistsError as e:
            failure_probability = 0
            print(f"FileExistsError occurred: read operation - {e}.")
            print(f"File '{file_path}' already exists. Retrying...")
            retry_count += 1

        except PermissionError as e:  # add lock for backend !!!!!!!!
            failure_probability = 0
            print(f"PermissionError occurred: read operation - {e}. Retrying...")
            retry_count += 1
            time.sleep(delay)
            delay *= 2

        except IsADirectoryError or NotADirectoryError as e:
            failure_probability = 0
            print(f"IsADirectoryError OR NotADirectoryError occurred: read operation - {e} ")
            if os.path.isdir(file_path):
                file_path = input("This is directory not path, insert the correct path :")
                print("Retrying...")
            else:
                print("It's path not directory, Retrying...")
            retry_count += 1

        except IOError as e:
            failure_probability = 0
            print(f"An IOError occurred while READING the file: read operation - {e}")
            print("Retrying...")
            retry_count += 1
            time.sleep(delay)
            delay *= 2
    print(f"Failed to perform file operation after {max_retries} retries: read - {file_path}")
    return None
