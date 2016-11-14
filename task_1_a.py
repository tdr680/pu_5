#----------------------------------------------------------------------------------------
# task_1_a.py
#----------------------------------------------------------------------------------------

import csv
import os


class CsvReader(object):
    """
    class to read csv file
    self.fieldnames stores the column names
    self.data stores list of records loaded from file in sequence:
    [
        {'gender': 'f', 'number': '1', 'name': 'Abarna', 'year': '1993'},
        {'gender': 'f', 'number': '1', 'name': 'Abetare', 'year': '1993'},
        {'gender': 'f', 'number': '1', 'name': 'Abir', 'year': '1993'},
        ...
    ]
    """

    # Reads the CSV file with name filename
    def __init__(self, file_name):
        # check whether file_name exists
        if not os.path.isfile(file_name):
            print 'ERROR: "{0}" file not found'.format(file_name)
            exit()
        # open file for reading and store as object variable
        file = open(file_name, 'r')
        # load content of the file as dictionary
        dict = csv.DictReader(file)
        self.data = []
        for rec in dict:
            self.data.append(rec)
        # store the field names as object variable
        self.fieldnames = dict.fieldnames

    # Checks if the field exists
    def has_field(self, field_name):
        return field_name in self.fieldnames

    # Returns the list of all fields
    def get_fields(self):
        return self.fieldnames

    # Returns the value from a field (column) and index (row)
    def get_value(self, field_name, row_idx):
        row = self.data[row_idx]
        return row[field_name]

    # Returns multiple vales from a field and a range of indices (rows)
    def get_values(self, field_name, row_range):
        result = []
        i = 0
        while i < len(self.data):
            if i in row_range:
                row = self.data[i]
                result.append(row[field_name])
            i += 1
        return result


#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    csv_reader = CsvReader('./baby_names.csv')
    print csv_reader.get_fields()         # returns ['year', 'name', 'gender', 'number']
    print csv_reader.get_value('year', 1) # returns 1993
    print csv_reader.has_field('name')    # True
    print csv_reader.has_field('test')    # False
    print csv_reader.get_values('name', range(0, 10))