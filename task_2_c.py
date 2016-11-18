#----------------------------------------------------------------------------------------
# task_2_c.py
#----------------------------------------------------------------------------------------


class Questionnaire(object):

    def __init__(self, questions):
        """
        :param questions: list of questions
        """
        self.questions = questions

    def add(self, question):
        """
        :param question: that't it
        :return: None
        """
        self.questions.append(question)

    def start(self):
        """
        :return: dict with the question keys as key and the answers as values
        """

        # go through our questions and ask everyone
        for question in self.questions:
            question.start()

        # dictionary to collect the answers
        result = {}

        # go through our questions and put the answer to the result dict
        for question in self.questions:
            result[question.key] = question.answer

        return result


#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    from task_2_b import Question

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
    # create Questionnaire object
    #

    questionnaire = Questionnaire([question_1, question_2, question_3])
    questionnaire.add(question_4)
    questionnaire.add(question_5)

    #
    # start the questionnaire and print the result
    #

    print questionnaire.start()

    # {'nationality': 'swiss', 'first_name': 'Karel', 'last_name': 'Capek', 'profession': 'student', 'age': '51'}