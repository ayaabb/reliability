import time

from backend.class_analysis_record_info import *


def init_analysis():
    return analysis_record_info()


def run_analyzer(analysis, file_path):
    print("analyze started :")

    while True:
        try:
            analysis.analyze_10_rabbit_records(file_path)
        except Exception as e:
            print("An error occurred during analysis:", e)

        time.sleep(20)  # Wait for 20 seconds before running the analysis again


