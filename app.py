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
    correct_answer = 'a'
    if user_guess == correct_answer:
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
    correct_answer = 'd'
    if user_guess == correct_answer:
        answers_correct.append(" Joe-Biden ")
        print("Nice! That was the correct answer. The answer is Joe Biden. ")
    else:
        print(
            "Incorrect. Leslie meets Joe Biden during her trip to the Nation's capital. .")

    return user_guess


def question_3():
    user_guess = int(input('''True or False. Parks and Recreation aired on ABC. Enter 1 for True or 0 for False
        Answer: '''))
    correct_answer = 0
    if user_guess == correct_answer:
        answers_correct.append(user_guess)
        print("Correct! It aired on NBC.")
        return 1
    else:
        print("Incorrect! It aired on NBC.")
        return 0


def question_4():
    user_guess = int(input('''True or False. 5000 candles in the wind is a song about a horse. Enter 1 for True or 0 for False
        Answer: '''))
    correct_answer = 1
    if user_guess == correct_answer:
        answers_correct.append(user_guess)
        print("Correct! Lil Sebastian is always in our hearts.")
        return 1
    else:
        print("Incorrect.")
        return 0


def question_5():
    user_guess = int(input(''' How many ex-wifes does Ron Swanson have?
    Answer: '''))
    correct_answer = 2
    if user_guess == correct_answer:
        answers_correct.append(user_guess)
    else:
        print("Ron actually had 2 ex-wives, both named Tammy.")
    return user_guess


def question_6():
    user_guess = int(input(''' How many seasons of Parks and Recreation aired on television?
    Answer: '''))
    correct_answer = 7
    if user_guess == correct_answer:
        answers_correct.append(user_guess)
    else:
        print("Wrong")
    return user_guess


if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    print("You got " + str(len(answers_correct)) + " answers correct.")
