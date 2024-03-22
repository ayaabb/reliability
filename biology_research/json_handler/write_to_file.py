import json
import msvcrt
import os
import random
import time


failure_probability = 0
delay = 1
max_retries = 3


def write_json_data(file_path, json_data):
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
                with open(file_path, 'w') as file:
                    # Acquire an exclusive lock for writing
                    # msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 2)

                    json.dump(json_data, file, indent=4)
                if failure_probability < 1.0:  # Cap the failure probability at 100%
                    failure_probability += 0.05  # Increase failure probability
                print('write operation-failure_probability after: ', failure_probability)
                return True
        except FileNotFoundError as e:
            # Perform file creation silently
            print(f"FileNotFoundError occurred : write operation - {e}.")
            failure_probability = 0  # Reset failure probability upon failure
            if not os.path.isfile(file_path):
                with open(file_path, "w") as _:
                    pass
                print("Error fixed,File Created successfully, Retrying...")
            else:
                print("File already exists, Retrying...")
            retry_count += 1


        except FileExistsError as e:
            failure_probability = 0
            print(f"FileExistsError occurred: write operation - {e}.")
            print(f"File '{file_path}' already exists. Retrying...")
            retry_count += 1

        except PermissionError as e:  # add lock for backend !!!!!!!!
            failure_probability = 0
            print(f"PermissionError occurred:  write operation - {e}. Retrying...")
            retry_count += 1
            time.sleep(delay)
            delay *= 2

        except IsADirectoryError or NotADirectoryError as e:
            failure_probability = 0

            print(f"IsADirectoryError OR NotADirectoryError occurred:  write operation - {e} ")

            if os.path.isdir(file_path):
                file_path = input("This is directory not path, insert the correct path :")
                print("Retrying...")
            else:
                print("It's path not directory, Retrying...")
            retry_count += 1

        except IOError as e:
            failure_probability = 0
            print(f"An IOError occurred while writing on file:  write operation - {e}")
            print("Retrying...")
            retry_count += 1
            time.sleep(delay)
            delay *= 2

    print(f"Failed to perform file operation after {max_retries} retries: write - {file_path}")
    return False
