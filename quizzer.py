# The random module is needed for this, in order to pick random questions
import random

def load_questions_and_answers(file_name):
    '''
    The function loads questions and answers from the file_name into a dictionary.
    Parameter:
      file_name: A string, the name of the file to load
    Returns a dictionary mapping questions (strings) to answers (also strings)
    '''
    qa = {}
    file = open(file_name, 'r')
    for line in file:
        line = line.strip('\n')
        components = line.split('|||')
        question = components[0]
        answer = components[1]
        qa[question] = answer
    return qa
        
def get_random_question(qa):
    '''
    This functions gets a random question from the question/answer dictionary.
    Parameter:
      qa: A dictionary mapping questions to answers.
    Returns a strings, the randomly-selected question.
    '''
    keys = list(qa.keys())
    index = random.randint(0, len(keys) - 1)
    key = keys[index]
    return key

def ask_question(qa):
    '''
    This function is responsible for asking the user q question.
    If the user gets it right, the question should be removed from the dictionary
    Parameter:
      qa: A dictionary mapping questions to answers.
    Returns True if the questions was answered correctly, False otherwise.
    '''
    question = get_random_question(qa)
    print(question)
    response = input('Enter response: ')
    if response == qa[question]:
        print('correct!')
        del qa[question]
        return True
    else:
        print('incorrect!')
        return False

def main():
    '''
    This is the main function.
    It contains the main loop for going through the quiz.
    After the quiz is completed, it prints a summary and then returns.
    '''
    file_name = input('What is the name of the QA file? ')
    number_of_questions = int(input('How many questions should be asked? '))
    questions_answers = load_questions_and_answers(file_name)
    correct_count = 0
    for i in range(number_of_questions):
        correct = ask_question(questions_answers)
        if correct:
            correct_count += 1
    print('You got', correct_count, 'out of', number_of_questions, 'correct.')
    print('Your percentage grade: ' + 
      str(correct_count / number_of_questions * 100) + '%')

main()

