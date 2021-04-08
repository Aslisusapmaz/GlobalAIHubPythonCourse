# Explain your work

# Answer Part1
# Taking input form user
username = input("Enter Username: ")
password = input("Enter Password: ")

# Checking values
if username == "asli" and password == "Hi":
    print("You were successful")
else:
    print("You were not successful")

# Answer Part2
value = {"username": input("Enter Username: "), "password": input("Enter Password : ")}  # defining dictionary
if value["username"] == "asli" and value["password"] == "Hi":
    print("You were successful")
else:
    print("You were not successful")
