with open("Teams.txt", "a") as file:
    file.write("This is a new line\n")

with open("Teams.txt", "r") as file:
    file_contents = file.read()
    print("File Contents after Adding a New Line:")
    print(file_contents)

with open("Teams.txt", "a") as file:
    file.write("This is a new line\n")

with open("Teams.txt", "r") as file:
    file_contents = file.read()
    print("File Contents after Adding a New Line:")
    print(file_contents)
