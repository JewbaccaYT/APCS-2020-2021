from random import choice
from os import system, name
import time
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

responses = ["As I see it, yes.", "Ask again later.", "Outlook not so good.", "My reply is no.",
             "Meditate and ask again", "It's hazy, try again.", "My sources say no.", "It is decidedly so."]
loading = ["Thinking.", "Thinking..", "Thinking..."]
gingerbread_man = True

print("You shook your ball.")
while gingerbread_man:
    question = input("What is your question?: ")
    for stage in loading:
        print(stage)
        time.sleep(.4)
        clear()
    print(choice(responses))
    play_again = input("Is this answer satisfactory?: ").capitalize()
    if play_again == "Yes":
        print("See you later, crocodile.")
        gingerbread_man = False
    else:
        print("You shake your ball again.")
