'''
This first block of code is a comment,
you can tell because it's got the 3 ' signs
at the top and bottom
'''

#this is a one line comment

"""
This also works for comments
"""

'''
Programming holds varibles in much the same way
math varibles work. 
'''
first_variable = 1
first_boolean = True
first_char = 'A'
first_string = "Hello world"

#These two lines do the same thing
print("Hello world")
print(first_string)

new_string = first_string + "! I am your new lord and Master!" 
#'i can't decide' plays in background
print(new_string)


if 4 < 10:
    print("4 is less than 10")


the_answer = 101
if the_answer >= 42:
    print("You are wise young padawan")
else:
    print("You have much to learn")


age = 0
while age < 18:
    print("You are a child, you are", age, "years old")
    age += 1
    # age = age + 1
print("You are now an adult!")

for number in range(14):
    #range(10) == 0,1,2...9
    print("There are", number, "dwarves in bilbo's house")


import math

print(math.pi)

name = input("What is your name?\n")
while True:
    print("hey,", name)
    age = input("What is your age?\n")
    age = int(age)
    if age < 1200:
        print("You are still younger than a certain Doctor")
    else:
        print("Age doesn't mean beauty, just look at the last human")
        break

if name == "David" or name == "Sarah":
    print("Thanks for coming, please come again")

