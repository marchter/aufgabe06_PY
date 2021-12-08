class Question:
    def __init__(self, question, level, answers, index):
        self._question = question
        self._level = level
        self._answers = answers
        self._index = index

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
