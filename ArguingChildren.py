# be sure to a random import of choice
# generate some questions for the annoying kid to ask
# create your while loop (ex. while answer != "just because":
#     answer = input("why?: ").strip().lower())
# generate a print statement that will mark the end

import random

annoying_questions = ["Why are you tall?", "Why is the sky blue?", "Why do I have to go to school?",
                      "Why can't I do this?"]
kid_satisfied = False

while not kid_satisfied:
    print(random.choice(annoying_questions))
    answer = input().capitalize()
    if answer == "Just because":
        kid_satisfied = True
        print("Well that kid was annoying")


