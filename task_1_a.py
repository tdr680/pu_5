#----------------------------------------------------------------------------------------
# task_1_a.py
#----------------------------------------------------------------------------------------

import csv
import os


class CsvReader(object):

    # Reads the CSV file with name filename
    def __init__(self, file_name):
        # check whether file_name exists
        if not os.path.isfile(file_name):
            print 'ERROR: "{0}" file not found'.format(file_name)
            exit()
        # open file for reading
        file = open(file_name, 'r')
        # store dictionary in object variable "dict"
        self.dict = csv.DictReader(file)

    # Checks if the field exists
    def has_field(self, field_name):
        pass

    # Returns the list of all fields
    def get_fields(self):
        return self.dict.fieldnames

    # Returns the value from a field (column) and index (row)
    def get_value(self, field_name, row_idx):
        current_rec = None
        idx = 0
        for rec in self.dict:
            if idx == row_idx:
                current_rec = rec
            idx += 1
        return current_rec[field_name]

    # Returns multiple vales from a field and a range of indices (rows)
    def get_values(self, field_name, row_range):
        pass



#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    csv_reader = CsvReader('./baby_names.csv')
    print csv_reader.get_fields()         # returns ['year', 'name', 'gender', 'number']
    print csv_reader.get_value('year', 1) # returns 1993
    print csv_reader.has_field('name')    # True
    print csv_reader.has_field('test')    # False

