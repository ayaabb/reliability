from json_handler.read_from_file import read_json_data
from json_handler.write_to_file import write_json_data


class analysis_record_info:
    def __init__(self):
        self.num_records_analyzed = 0
        self.total_alive_rabbits = 100

    def analyze_10_rabbit_records(self, file_path):
        """read the records data , check if there are 10 records at least since last time it read,
           then check if the death number are valid for each record,if not it deletes the record
           if so it updates the total alive rabbits and record total number and num records analyzed
         """
        try:
            json_data = read_json_data(file_path)
            if json_data is None:
                raise Exception("read operation failed while analyzing the records")
            indexes_to_remove = self.check_10_records(json_data)
            updated_data = json_data
            if len(indexes_to_remove) > 0:
                updated_data = self.delete_invalid_records(json_data, indexes_to_remove)
            write_success = write_json_data(file_path, updated_data)
            if not write_success:
                raise Exception("write operation failed while analyzing the records")
            self.num_records_analyzed = 10 - len(indexes_to_remove)
            print(
                f"Analyzing rabbit records...\nTotal records analyzed: {self.num_records_analyzed},"
                f"\nTotal alive rabbits: {self.total_alive_rabbits}")
        except (IndexError, ValueError) as e:
            print(e)
        except Exception as e:
            print(e)

    @staticmethod
    def delete_invalid_records(json_data, indexes_to_remove):

        for index in indexes_to_remove:
            json_data.pop(index)
        return json_data

    def check_10_records(self, data):
        """Checks every 10 records if the number of deaths in a record is bigger than the
           total number of living rabbits then deletes the record and ignore it in the analysis
           and updates the total number of alive rabbits
           parameters: (list of dictionaries ) data of records,
           (int) num_records_analyzed
           (int) total_alive_rabbits since last analyzed
           returns: list:  indexes_to_delete
         """
        list_indexes_to_delete = []
        if data is None:
            raise ValueError("The file is still empty,try again later")
        if len(data) - self.num_records_analyzed < 10:
            raise IndexError("Records file includes less than 10 record since last analyzed record, try again later")
        for i in range(self.num_records_analyzed, self.num_records_analyzed + 10):
            _, deaths_births = next(iter(data[i].items()))
            if deaths_births[0] > self.total_alive_rabbits:
                list_indexes_to_delete.append(i)
            else:
                self.total_alive_rabbits += deaths_births[1] - deaths_births[0]
        return list_indexes_to_delete
