def valid_input(prompt, options):
    '''Ensures user input is within valid options. '''
    user_input = input(prompt)
    while user_input not in options:
        print("Invalid option")
        user_input = input(prompt)
    return user_input


answers_correct = []


def question_1():
    user_guess = input(''' The series is set in the parks department of a fictional town called Pawnee. In what state is Pawnee in?
            a. Indiana
            b. Texas
            c. Kentucky
            d. South Carolina
            e. New York
        Answer: ''')
    if user_guess == 'A' or 'a':
        answers_correct.append("Indiana ")
        print("Nice! That was the correct answer.The fictional town of Pawnee is located in Indiana")
    else:
        print("Incorrect. The fictional town of Pawnee is located in Indiana.")
    return user_guess


def question_2():
    user_guess = input(''' Which former Presidential candidate did Leslie encounter in the Hay Adams Hotel in the episode 'Miss Knope Goes to Washington?
            a. Mitt Romney
            b. Al Gore
            c. John Mccain 
            d. Joe Biden
            e. Dick Cheney
        Answer: (Type in letter of answer) ''')
    if user_guess == 'D' or 'd' or "Joe Biden":
        answers_correct.append(" Joe-Biden ")
        print("Nice! That was the correct answer. The answer is Joe Biden. ")
    else:
        print(
            "Incorrect. Leslie meets Joe Biden during her trip to the Nation's capital. .")
    return user_guess


def question_3():
    user_guess = input('''True or False. Parks and Recreation aired on ABC. Enter 1 for True or 0 for False
        Answer: ''')
    if user_guess == '1':
        bool("0" or "false")
        answers_correct.append(" Joe-Biden ")
        print("Nice! That was the correct answer. The answer is Joe Biden. ")
    else:
        bool()
        print("Incorrect. Leslie meets Joe Biden during her trip to the Nation's capital. ")
    return user_guess


question_1()
question_2()
question_3()
print(answers_correct)
