import time
from os import system, name
import random
'''' ll = input("Lowercase letter: ")
ul = input("Uppercase Letter: ")
print(ll == ul)

students = {
    "freshman": ["Mike", "John", "Melissa", "Eric", "Cindy"],
    "sophomores": ["Joan", "Christine", "Danny", "Martin"]
}


for key in students.keys():
    for name in students[key]:
        if "o" in name:
            print(name)'''

(lambda func: func(func))((lambda func:(((lambda inp: ([(print("Thinking" + "".join(["." for x in range((y % 3) + 1)])),time.sleep(.4),(lambda _: system('cls') if name == 'nt' else system('clear'))(None)) for y in range(9)],print(inp, random.choice(["No", "Yes", "Definitely", "Maybe", "Likely", "Unlikely", "Very Likely", "Very Unlikely"]))))(input("What question would you like to ask? "))),func(func) if input("\nWould you like to play again? ").strip().lower() in ["y", "yea", "yes", "ye", "yep"] else None)))

