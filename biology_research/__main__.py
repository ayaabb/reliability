import multiprocessing
import sys
from run_backend import *
from run_sensor import *


def main(file_path):
    analysis = init_analysis()
    process1 = multiprocessing.Process(target=generate_all_records, args=(file_path,))
    process2 = multiprocessing.Process(target=run_analyzer, args=(analysis, file_path))

    # Start both processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()


if __name__ == '__main__':
    path_file = sys.argv[1]
    main(path_file)
