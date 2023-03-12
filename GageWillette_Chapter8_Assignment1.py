#Write a program that gets a string containing a person’s first, middle, and last names,
# and then display their first, middle, and last initials. For example, if the user enters John William Smith the program should display J. W. S.

def main():
    fullName = input("Enter your full name (ex. \"John William Smith\"): ")
    names = fullName.split()
    initials = ""
    for name in names:
        initials += str(name[0].capitalize()) + ". " 
    print("Intials: " + initials)


main()