import random
import time

from sensor.store_record import store_record
from sensor import generate_record

random_min_records = 100
random_max_records = 300
random_min_sleep = 5
random_max_sleep = 10


def generate_all_records(file_path):
    print("generate started :")
    num_of_records = random.randint(random_min_records, random_max_records)
    for i in range(num_of_records):
        record, time_ = generate_record()
        store_record(file_path, record, time_)
        time.sleep(random.randint(random_min_sleep, random_max_sleep))
