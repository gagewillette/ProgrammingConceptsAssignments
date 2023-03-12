#this function accepts an input string of three words. (First Name, Middle Name, Last Name)
#the function will then output the initials of each of the names

#define main
def main():
    #attain user input
    fullName = input("Enter your full name (ex. \"John William Smith\"): ")
    #split names into name array
    names = fullName.split()

    #check if name array is more than three indicies
    if len(names) != 3:
        #raise error if input is wrong
        raise ValueError("Your name input must be three words! (ex. \"John William Smith\")")

    #accumulator string
    initials = ""
    #loop thru name array
    for name in names:
        #add first letter of each name to accumulator string
        initials += str(name[0].capitalize()) + ". " 
    #print 2 console
    print("Intials: " + initials)


main()