from flask import Flask, render_template
import random

app = Flask(__name__)


questions = {
            'Who is president of USA?':
            ('\na. Myslef\nb. His dad\nc. His mom\nd. Barack Obama\n', 'd'),
            'What is the capital of USA?':
            ('\na. Zimbabwe\nb. New York\nc. Washington\nd. Do not exist', 'c')
            }

def ask_question(questions):
    #Asks random question from 'questions 'dictionary and returns
    #players's attempt and correct answer.

    item = random.choice(list(questions.items()))
    question = item[0]
    (variants, answer) = item[1]
    print(question, variants)
    attempt = input('\nHit \'a\', \'b\', \'c\' or \'d\' for your answer\n')
    return render_template (attempt, answer)

# Questions loop
tries = 0
for questions_number in range(5):
    while True: # Asking 1 question
        attempt, answer = ask_question(questions)
        if attempt not in {'a', 'b', 'c', 'd'}:
            print('INVALID INPUT!!! Only hit \'y\' or \'n\' for your response')
        elif attempt == answer:
            print('Correct')
            stop_asking = False
            break
        elif tries == 1: # Specify the number of tries to fail the answer
            print('Incorrect!!! You ran out of your attempts')
            stop_asking = True
            break
        else:
            tries += 1
            print('Incorrect!!! Try again.')
    if stop_asking:
        break

if __name__ == '__main__':
    app.run(debug=True)

