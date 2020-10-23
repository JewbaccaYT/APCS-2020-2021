# First, pick any two numbers you like and store them in two separate variable, num1 & num2
# Next, create a valid condition that will check if num1 is greater than num2
# Next, create a second condition that will check if num1 is equal to the num2
# Finally, create a third condition that will check if num2 is greater than num1

num1 = int(input("Pick a number: "))
num2 = int(input("Pick another number: "))

if num1 > num2:
    print("First Number is greater")
elif num1 == num2:
    print("Numbers are equal")
elif num1 < num2:
    print("First Number is lesser")