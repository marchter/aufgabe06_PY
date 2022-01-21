
import time
from model import Question
from threading import Thread
from playsound import playsound
import sys

# INDEX = WELCHE ANTWORT RICHTIG IST

questions = []
level = 0


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
        print("The correct answer was " + question.get_answers()[question.get_index()])
        time.sleep(2)
        sys.exit()


def play_effect(effect):
    play_thread = Thread(target=lambda: playsound("sounds/" + effect))
    play_thread.daemon = True
    play_thread.start()



def print_game():
    play_effect("lets_play.wav")
    question = Question.get_rand_question(level)
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
    Question.shuffle_answers()
    play_effect("background.wav")


    #TODO: set background volume and stop background music when other effect is played AND handle win(correct answer on question 4)

    while level < 5:
        print_game()
    if level == 5:

        print("Oh there isn't a next question! YOU WON")

