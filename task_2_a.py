#----------------------------------------------------------------------------------------
# task_2_a.py
#----------------------------------------------------------------------------------------


class Customer(object):

    def __init__(self, first_name, last_name, age, nationality, profession):
        """
        :param first_name: string beginning with a upper case letter
        :param last_name: string beginning with a upper case letter
        :param age: string only containing digits
        :param nationality: string representing a valid nationality (you can check for only a subset like: 'swiss', 'american', 'german')
        :param profession: string which is either 'student', 'doctor' or 'nurse' (or 'captain')
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.profession = profession


#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    customer_1 = Customer('James', 'Kirk', '38', 'american', 'captain')
    customer_2 = Customer('Leonard', 'McCoy', '42', 'swiss', 'doctor')
