#the following program asks the user for their age and validates that it is a number.
#the program will then run their age against a series of conditions, stopping on the met condition and printing it to console


#accept user input (int only)
age = int(input("Please enter your age: "))

#validate age is > 0
if age < 0:
    print("Your age can not be less than zero!")
#check if person is younger than 1
elif age <= 1:
    print("You are an infant!")
#check if person is younger than 13
elif age < 13:
    print("You are a child!")
#check if person if younger than 20
elif age < 20:
    print("You are a teengaer!")
#check if person is older than 20
else:
    print("You are an adult!")
