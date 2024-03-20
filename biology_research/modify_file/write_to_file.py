import json
import os


def write_to_file(record, time_):
    if not os.path.isfile("db/records.json"):
        with open("db/records.json", "w") as json_file:
            json.dump([{time_: record}], json_file, indent=4)
    else:
        with open("db/records.json", "r") as json_file:
            data = json.load(json_file)
        data.append({time_: record})
        with open("db/records.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
