"String Variables Exercise"
# ask a user to enter their first name and store it in a variable
# ask a user to enter their last name and store it in a variable
# print their full name
# Make sure you have a space between first and last name
# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase

'''Numeric Variables Exercise'''
# Ask a user to enter a number
# Ask a user to enter a second number
# Calculate the total of the two numbers added, subtracted, multiplied and divided
# Be sure to have a print statement for each operation

"Combining Both to Create an Essay"
# Give me an brief paragraph that will include details about you
# Be sure to include variables for all colleges you are applying to
# What your GPA is and a calculation that will demonstrate how to increase it
# Finally, which activities you are involved in
# The purpose of this will see how well you can generate a paragraph through print statements
# string and numeric variables
# Comments should include brief explanations of different sections of your code

# Name Input and Print
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
fullname = (first_name.capitalize(), last_name.capitalize())

# Number Input and Calculations
first_num = float(input("Enter a number?: "))
second_num = float(input("Enter another number?: "))
# List for all possible combinations of basic math with the two numbers
answers = [first_num + second_num,
           first_num * second_num,
           first_num - second_num,
           first_num / second_num,
           first_num - second_num,
           first_num / second_num]

print(str(first_num) + ' + ' + str(second_num) + " = " + str(answers[0]))
print(str(first_num) + ' * ' + str(second_num) + " = " + str(answers[1]))
print(str(first_num) + ' - ' + str(second_num) + " = " + str(answers[2]))
print(str(first_num) + ' / ' + str(second_num) + " = " + str(answers[3]))
print(str(first_num) + ' - ' + str(second_num) + " = " + str(answers[4]))
print(str(first_num) + ' / ' + str(second_num) + " = " + str(answers[5]))

# Essay

# List includes the names of the colleges I want to go to as of now, using .join to list them out in the Print Statement
colleges = ["Berklee College of Music", "Steven's Institute of Technology", "Oberlin College of Arts and Sciences",
            "Oberlin Conservatory", "Purchase College"]
# Cumulative Percentage and GPA calc to a 4 point scale
cumulative = 77.03
gpa = 2.3
print("My name is " + " ".join(fullname) + " and I am 17 years old.\n"
                                           "I want to apply to " + ", ".join(colleges) + "." + "\n"
                                            "My GPA could be better, as it is currently a " + str(gpa) + '.\n' +
                                            "I am trying to do better in my classes this year, "
                                            "and I hope that my gpa will increase and colleges will se that I am trying harder" + '\n'
                                            "I love playing, writing, and listening to music, and I would love to get a job that involves that somehow. \n"
                                            + "I also enjoy working with computers, so Audio Technology is a field that I am potentially interested in.")