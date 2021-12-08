import random
from model import Question

# INDEX = WELCHE ANTWORT RICHTIG IST

fName = "millionaire.txt"
questions = []


def read_questions():
    questions = []
    f = open(fName, "r")

    for line in f.readlines():
        questions.append(line.split("\t")[1])
    f.close()
    return questions


def read_question(line):
    return read_questions()[line]


def get_rand_question(level, questions):
    f = open(fName, "r")
    pool = []
    i = 0
    for q in f.readlines():
        if q.split("\t")[0] == str(level):
            pool.append(questions[i])
        i = i + 1
    f.close()
    return pool[random.randint(0, len(pool))]


def set_questions():
    f = open(fName, "r")
    i = 0
    for q in f.readlines():
        line = q.split("\t")
        questions.append(Question(line[1], line[0], [(line[2]), (line[3]), (line[4]),  line[5].replace("\n","")], 1))
        i = i + 1


def shuffle_answers():
    for q in questions:
        q.set_index(random.randint(0, len(q.get_answers())))
        q.set_answers((q.get_answers())) #TODO: hier antwort auf index schieben



set_questions()

shuffle_answers()


for a in questions[0].get_answers():
    print(a)

# print(questions[1])
# TODO: question anlegen

# TODO: Antworten mischeln(Index zufällig wählen und die 1. antwort auf diese position schieben)
