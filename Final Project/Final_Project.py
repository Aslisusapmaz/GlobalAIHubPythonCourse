print("Knowledge competition program")

# initialise the score
score = 0

print("1) What is the maximum possible length of an identifier?")
print("16")
print("32")
print("64")
print("None of these above")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "d":
    score += 1

print("2) Who developed the Python language?")

print("Zim Den")
print("Guido van Rossum")
print("Niene Stom")
print("Wick van Rossum")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "b":
    score += 1

print("3) In which year was the Python language developed?")

print("1995")
print("1972")
print("1981")
print("1989")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "d":
    score += 1

print("4) In which language is Python written?")

print("English")
print("PHP")
print("C")
print("All of the above")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "c":
    score += 1

print("5) Which one of the following is the correct extension of the Python file?")

print(".py")
print(".python")
print(".p")
print("None of these")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "a":
    score += 1

print("6) In which year was the Python 3.0 version developed?")

print("2008")
print("2000")
print("2010")
print("2005")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "a":
    score += 1

print("7) What do we use to define a block of code in Python language?")

print("Key")
print("Brackets")
print("Indentation")
print("None of these")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "c":
    score += 1

print("8) Which character is used in Python to make a single line comment?")

print("/")
print("//")
print("#")
print("!")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "c":
    score += 1

print("9) Which of the following statements is correct regarding the object-oriented programming concept in Python?")

print("Classes are real-world entities while objects are not real")
print("Objects are real-world entities while classes are not real")
print("Both objects and classes are real-world entities")
print("All of the above")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "b":
    score += 1

print("10) What is the method inside the class in python language?")

print("Object")
print("Function")
print("Attribute")
print("Argument")

choice = input("\nEnter the choice among a,b,c and d : ")
if choice.lower() == "b":
    score += 1

# now check if score is more than 5
print("Result : ")
if score > 5:
    print("\nYou have successfully cleared the test")
else:
    print("\nUnsuccessful in the test")
