acronym = input("Which acronym would you like to add?\n")
definition = input(f"What is the definition of {acronym}?")

with open("acronyms.txt", "w") as file:
    file.write(f"{acronym} - {definition}")
