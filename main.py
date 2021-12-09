import random
from model import Question
from threading import Thread
from playsound import playsound

# INDEX = WELCHE ANTWORT RICHTIG IST

fName = "millionaire.txt"
questions = []
level=0


def read_questions():
    q = []
    f = open(fName, "r")

    for line in f.readlines():
        q.append(line.split("\t")[1])
    f.close()
    return q


def read_question(line):
    return read_questions()[line]


def get_rand_question(level):
    f = open(fName, "r")
    pool = []
    i = 0
    for q in questions:
        if level == int(q.get_level()):
            pool.append(questions[i])
        i = i + 1
    f.close()
    return pool[random.randint(0, (len(pool) - 1))]


def set_questions():
    f = open(fName, "r")
    i = 0
    for q in f.readlines():
        line = q.split("\t")
        questions.append(Question(line[1], line[0], [(line[2]), (line[3]), (line[4]), line[5].replace("\n", "")], 1))
        i = i + 1


def shuffle_answers():
    for q in questions:
        q.set_index(random.randint(0, len(q.get_answers()) - 1))
        answers = q.get_answers()
        ind = q.get_index()
        answers[0], answers[ind] = answers[ind], answers[0]
        q.set_answers(answers)
        q.set_answers((q.get_answers()))


def handle_input(input, question):
    global level

    if input == question.get_index():
        print("You chose the right answer! Lucky!")
        print("------------------------------------------------------------")
        print("NEXT QUESTION")
        level = level + 1

    else:
        play_effect("lose.wav")
        print("YOU LOST! Better luck next time!")
        print("The true answer was "+question.get_answers()[question.get_index()])
        level = level + 6

def play_effect(effect):

    play_thread = Thread(target=lambda: playsound("sounds/"+effect))
    play_thread.start()


def print_game():
    play_effect("lets_play.wav")
    question = get_rand_question(level)
    print("------------------------------------------------------------")
    print("Your current difficulty is: " + str(level) + "\n")
    print(question.get_question())
    i = 0
    for a in question.get_answers():
        print('\t(%d), %s' % (i, a))
        i = i + 1
    print("\nWhat answer do you choose? Think carefully!\n")
    handle_input(int(input()), question)

if __name__ == '__main__':
    set_questions()
    shuffle_answers()
    #play_effect("background.wav")
    #TODO: fix background music

    while level <= 5:
        print_game()