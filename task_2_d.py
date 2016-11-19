#----------------------------------------------------------------------------------------
# task_2_d.py
#----------------------------------------------------------------------------------------

from task_2_a import Customer
from task_2_b import Question
from task_2_c import Questionnaire


class Application:
    def __init__(self):
        self.questionnaire = self.create_questionaire()
        self.customers = []

    def create_questionaire(self):
        # TODO: define the methods for checking that the different inputs are valid, that
        # the necessary conditions are valid as defined at the beginning of the exercise

        # name has to contain just letters
        def is_name(user_input):
            if user_input.isalpha():
                return True
            else:
                return False

        # number has to contain just digits
        def is_number(user_input):
            if user_input.isdigit():
                return True
            else:
                return False

        # nationality has to be one of those three
        def is_nationality(user_input):
            if user_input in ('swiss', 'american', 'german'):
                return True
            else:
                return False

        # profession has to be one of those four
        def is_profession(user_input):
            if user_input in ('student', 'doctor', 'nurse', 'captain'):
                return True
            else:
                return False

        questionnaire = Questionnaire()
        questionnaire.add(Question("first_name", "What is the customer's first name?", is_name))
        questionnaire.add(Question("last_name", "What is the customer's last name?", is_name))
        questionnaire.add(Question("age", "What is the customer's age?", is_number))
        questionnaire.add(Question("nationality", "What is the customer's nationality?", is_nationality))
        questionnaire.add(Question("profession", "What is the customer's profession?", is_profession))
        return questionnaire

    def start(self):
        # TODO: print a Hello message to the user and the initial help instructions
        self.print_help()

        # TODO: ask the user what he would like to do, the user should input one
        # of the 3 commands described in the exercise. If it is a valid command,
        # handle it, otherwise print an error message and the help instructions
        while (True):
            user_input = raw_input("Action: ")
            if user_input == "add":
                self.register_new_customer()
            elif user_input == "list":
                self.list_customers()
            elif user_input == "exit":
                exit()
            else:
                self.print_help()

    def print_help(self):
        print(
        "You can type one of the following actions:\n\nadd - Add a new customer\nlist - list the existing customers\nexit - exit the database\n")

    def register_new_customer(self):
        tmp = self.questionnaire.start()
        # if you don't understand what happens here, check this link:
        # https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
        self.customers.append(Customer(**tmp))
        print("You successfully registered a new customer.")

    def list_customers(self):
    # TODO: list all the customers registered so far, by printing their first and last
    # names, the age, profession and nationality
        for customer in self.customers:
            print "{0} {1} {2} {3} {4}".format(customer.first_name,
                                               customer.last_name,
                                               customer.age,
                                               customer.profession,
                                               customer.nationality)


# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
    Application().start()
