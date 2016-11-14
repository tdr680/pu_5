#----------------------------------------------------------------------------------------
# task_1_b.py
#----------------------------------------------------------------------------------------

import csv
import os


class CsvWriter(object):

    # Gets the fields of the CSV
    def __init__(self, columns):
        pass

    # Checks if the field exists
    def has_field(self, field_name):
        pass

    # Returns a list of all fields
    def get_fields(self):
        pass

    # Adds a row of values
    def add_row(self, record):
        pass

    # Sets the value of the field (column) and index (row)
    def set_value(self, field_name, row_idx, value):
        pass

    # Writes the content to a file with name filename
    def write_csv(self, file_name):
        pass



#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    csv_writer = CsvWriter(['name', 'age'])
    csv_writer.add_row(['Bob', 21])     # adds new data
    csv_writer.set_value('age', 0, 16)  # sets the age of Bob to 16
    csv_writer.write_csv('test.csv')    # writes file test.csv with data
