#----------------------------------------------------------------------------------------
# task_1_b.py
#----------------------------------------------------------------------------------------

import csv


class CsvWriter(object):

    # Gets the fields of the CSV
    def __init__(self, columns):
        self.data = []
        self.fieldnames = columns

    # Checks if the field exists
    def has_field(self, field_name):
        return field_name in self.fieldnames

    # Returns a list of all fields
    def get_fields(self):
        return self.fieldnames

    # Adds a row of values
    def add_row(self, record):
        # a = ["d", "e"]
        # b = [1, 2]
        # zip(a, b) --> [('d', 1), ('e', 2)]
        # dict([('d', 1), ('e', 2)]) --> {'d': 1, 'e': 2}
        row = dict(zip(self.fieldnames, record))
        self.data.append(row)

    # Sets the value of the field (column) and index (row)
    def set_value(self, field_name, row_idx, value):
        row = self.data[row_idx]
        row[field_name] = value

    # Writes the content to a file with name filename
    def write_csv(self, file_name):
        file = open(file_name, "w")
        writer = csv.DictWriter(file, fieldnames=self.fieldnames)
        writer.writeheader()
        for row in self.data:
            writer.writerow(row)



#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    csv_writer = CsvWriter(['name', 'age'])
    csv_writer.add_row(['Bob', 21])     # adds new data
    csv_writer.set_value('age', 0, 16)  # sets the age of Bob to 16
    csv_writer.add_row(['Carl', 22])    # adds new data
    csv_writer.add_row(['Eve', 21])     # adds new data
    csv_writer.write_csv('test.csv')    # writes file test.csv with data
