
from datetime import datetime
import random


min_rand = 10
max_rand = 99





def generate_record():
    num_deaths = random.randint(min_rand, max_rand)
    num_births = random.randint(min_rand, max_rand)
    curr_time = datetime.now().replace(microsecond=0).isoformat()
    return [num_deaths, num_births], curr_time
