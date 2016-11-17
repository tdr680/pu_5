#----------------------------------------------------------------------------------------
# task_2_b.py
#----------------------------------------------------------------------------------------


class Question(object):

    def __init__(self, key, question, verify):
        """
        :param key: A unique string to identify the question
        :param question: The question displayed on the command line
        :param verify: A function which checks if a string meets certain requirements
        """
        self.key = key
        self.question = question
        self.verify = verify
        self.answer = ""

    def start(self):
        # ask user to input the answer to our question
        user_input = raw_input(self.question)
        # 'self.verify' is function with one parameter, returning boolean
        if self.verify(user_input):    # let's call the function
            self.answer = user_input   # function returns True (user's input is rubbish)
        else:
            print "Your answer doesn't make sense. Please try again."
            self.start()  # start again


#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    #
    # functions that are going to be passed to the Question objects
    #

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

    #
    # create five Question objects
    #

    question_1 = Question("first_name", "What is the customer's first name?", is_name)
    question_2 = Question("last_name", "What is the customer's last name?", is_name)
    question_3 = Question("age", "What is the customer's age?", is_number)
    question_4 = Question("nationality", "What is the customer's nationality?", is_nationality)
    question_5 = Question("profession", "What is the customer's profession?", is_profession)

    #
    # start every question
    #

    question_1.start()
    question_2.start()
    question_3.start()
    question_4.start()
    question_5.start()

