#print("Hello!")
#name = input("What is your name? ")
#print("Nice to meet you "+name)


age = input("How old are you? ")

#age must be a number, not a string
age = int(age)

print(str(age)+", is a good age")
#Add 10 to age
computerAge = int(age)+10
#computerAge must be a string, for adding purposes
computerAge = str(computerAge)
print("Hi yougster, I'm "+computerAge)

input("Press enter to quit")
