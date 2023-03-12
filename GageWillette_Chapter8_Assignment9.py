#

def main():
    
    #vowelCountInput = input("Enter a string for the vowel count: ")
    print(vowelCount(input("Enter a string for the vowel count: ")))
    #consonantCountInput = input("Enter a string for the vowel count: ")
    print(consonantCount(input("Enter a string for the consonant count: ")))
    #vowelConsonantCountInput = input("Enter a string for the vowel count: ")
    print(vowelConsonantCount(input("Enter a string for the vowel and consonant count: ")))

def vowelChecker(character):
    if len(character) > 1:
        raise ValueError("vowelChecker's parameter must be of a single character!")

    match str(character).lower():
        case "a":
            return True
        case "e":
            return True
        case "i":
            return True
        case "o":
            return True
        case "u":
            return True
    return False

def vowelCount(string):
    vowelCount = 0
    for letter in string:
        if vowelChecker(letter):
            vowelCount += 1

    return vowelCount

def consonantCount(string):
    consCount = 0
    for letter in string:
        if vowelChecker(letter) == False:
            consCount += 1

    return consCount

def vowelConsonantCount(string):
    consCount = 0
    vowelCount = 0
    for letter in string:
        if vowelChecker(letter):
            vowelCount += 1
            continue
        consCount += 1

    return ["Vowels: " + str(vowelCount), "Consonants: " + str(consCount)]

main()