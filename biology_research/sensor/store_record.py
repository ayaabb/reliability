import os
from json_handler.read_from_file import read_json_data
from json_handler.write_to_file import write_json_data


def store_record(file_path, record, time_):
    try:
        if not os.path.isfile(file_path):
            write_success = write_json_data(file_path, [{time_: record}])
            if not write_success:
                raise Exception("write operation failed while sorting a record")
        else:
            data = read_json_data(file_path)
            if data is None:
                raise Exception("read operation failed while sorting a record")
            data.append({time_: record})
            write_success = write_json_data(file_path, data)
            if not write_success:
                raise Exception("write operation failed while sorting a record")
    except Exception as e:
        print(e)
