import random
import time

from sensor import generate_record

random_min_records = 100
random_max_records = 300
random_min_sleep = 5
random_max_sleep = 10


def generate_all_records():
    num_of_records = random.randint(random_min_records, random_max_records)
    for _ in range(num_of_records):
        generate_record()
        time.sleep(random.randint(random_min_sleep, random_max_sleep))


generate_all_records()
