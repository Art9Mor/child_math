class Question:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def calculate_answer(self, operation):
        return str(int(eval(f'{self.num_1}{operation}{self.num_2}')))

    def check(self, operation, answer):
        right_answer = self.calculate_answer(operation)
        return right_answer == answer

    def ask_question(self, operator):
        print

    def __repr__(self):
        return f'{self.num_1} {self.num_2}'

# question = Question(6, 2)
#
# print(question.ask('*'))
