# class user_input:
#     def __init__(self):


# def valid_user_input(prompt, options):
#     '''Ensures user input is within valid options. '''
#     user_input = input(prompt)
#     while user_input not in options:
#         print("Invalid option")
#         user_input = input(prompt)
#     return user_input


# # class quiz_questions(valid_user_input):
# #     pass

# class Quiz:
#     def __init__(self, questions: list, answers: list):
#         self.questions = questions
#         self.correct_answers = answers
#         self.user_answers = []

#     def answer_question(self, answer):
#         self.user_answers.append(answer)

#     def grade(self):
#         answers_correct = 0
#         for i in range(len(self.user_answers)):
#             if self.correct_answers[i] == self.user_answers[i]:
#                 answers_correct += 1
#         return answers_correct / len(self.questions)


# def give_quiz(quiz: Quiz):
#     for question in quiz.questions:
#         a = valid_user_input(question)
#         quiz.answer_question(a)


# if __name__ == '__main__':
#     questions = []
#     answers = []
#     q = Quiz(questions, answers)
#     give_quiz(q)
#     print("You scored", q.grade())

def valid_input(prompt, options):
    '''Ensures user input is within valid options. '''
    user_input = input(prompt)
    while user_input not in options:
        print("Invalid option")
        user_input = input(prompt)
    return user_input


answers_correct = []


def question_one():
    user_guess = input(''' The series is set in the parks department of a fictional town called Pawnee. In what state is Pawnee in?
            a. Indiana
            b. Texas
            c. Kentucky
            d. South Carolina
            e. New York
        Answer: ''')
    if user_guess == 'a':
        answers_correct.append(user_guess)
        print("Nice! That was the correct answer.")
    else:
        print("Incorrect. The fictional town of Pawnee is located in Indiana.")


question_one()
