from random import random

class Question:
    global questions

    def __init__(self, question, level, answers, index):
        self._question = question
        self._level = level
        self._answers = answers
        self._index = index
        self.set_questions()

    def __str__(self):
        ret = self._question + " " + self._level + " " + str(self._answers) + " " + str(self._index)
        return ret

    def get_answers(self):
        return self._answers

    def set_index(self, index):
        self._index = index

    def get_index(self):
        return self._index

    def set_answers(self, answers):
        self._answers = answers

    def get_question(self):
        return self._question

    def get_level(self):
        return self._level

    def read_questions(self):
        fName = "millionaire.txt"
        q = []
        f = open(fName, "r")

        for line in f.readlines():
            q.append(line.split("\t")[1])
        f.close()
        return q

    def read_question(line):
        return Question.read_questions()[line]


    def get_rand_question(level):
        fName = "millionaire.txt"
        f = open(fName, "r")
        pool = []
        i = 0
        for q in questions:
            if level == int(q.get_level()):
                pool.append(questions[i])
            i = i + 1
        f.close()
        return pool[random.randint(0, (len(pool) - 1))]

    def set_questions(self):
        fName = "millionaire.txt"
        f = open(fName, "r")
        i = 0
        for q in f.readlines():
            line = q.split("\t")
            questions.append(
                Question(line[1], line[0], [(line[2]), (line[3]), (line[4]), line[5].replace("\n", "")], 1))
            i = i + 1

    def shuffle_answers():
        for q in questions:
            q.set_index(random.randint(0, len(q.get_answers()) - 1))
            answers = q.get_answers()
            ind = q.get_index()
            answers[0], answers[ind] = answers[ind], answers[0]
            q.set_answers(answers)
            q.set_answers((q.get_answers()))
