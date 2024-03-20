class last_read_record:
    def __init__(self):
        self.total_records = 0
        self.num_records_analyzed = 0
        self.total_alive_rabbits = 100

    def analyze_data_base(self):
        """read the records data , check if there are 10 records at least since last time it read,
           then check if the death number are valid for each record,if not it deletes the record
           if so it updates the total alive rabbits and record total number and num records analyzed
         """
