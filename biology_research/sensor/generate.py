from datetime import datetime
import random
# from modify_file.write_to_file import*

from modify_file import write_to_file

min_rand=10
max_rand=99

def generate_record():
    num_deaths = random.randint(min_rand, max_rand)
    num_births = random.randint(min_rand, max_rand)
    curr_time = datetime.now().replace(microsecond=0).isoformat()
    write_to_file([num_deaths, num_births], curr_time)
