age = input("What is your age? ")
age = int(age)+1
monthAge = age*12
dayAge = monthAge*365
hourAge = dayAge*24
minuteAge = hourAge*60
secondAge = minuteAge*60
secondAge = str(secondAge)
age = str(age)
print("You will be approximately "+secondAge+" seconds old on your next birthday, when you turn "+age)
input("Press enter to quit ")
