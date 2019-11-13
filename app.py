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
