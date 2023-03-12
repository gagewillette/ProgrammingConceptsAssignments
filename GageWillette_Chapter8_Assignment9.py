#this file contians three main function (vowelCount, consCount, vowelConsCount) 
#which will return the number of vowels, consonant, and vowels and consosnts, respectively
#the main helper function is vowelChecker() which checks if a input character is a vowel

#define main
def main():
    #get input for each function and run function
    vowelCount(input("Enter a string for the vowel count: "))
    consonantCount(input("Enter a string for the consonant count: "))
    vowelConsonantCount(input("Enter a string for the vowel and consonant count: "))

#define vowel check w character input paramter
def vowelChecker(character):
    #throw error if input is not a single character
    if len(character) > 1:
        raise ValueError("vowelChecker's parameter must be of a single character!")

    #swtich case for character value
    match str(character).lower():
        #check character against each vowel
        case "a":
            #return true if vowel
            return True
        case "e":
            return True
        case "i":
            return True
        case "o":
            return True
        case "u":
            return True
    #return false if consonant
    return False

#def vowel count
def vowelCount(string):
    #accumulator
    vowelCount = 0
    #loop thru input string
    for letter in string:
        #check if vowel
        if vowelChecker(letter):
            vowelCount += 1

    return vowelCount

def consonantCount(string):
    #accumulator
    consCount = 0
    #loop thru input string
    for letter in string:
        #check if NOT vowel
        if vowelChecker(letter) == False:
            consCount += 1

    return consCount

def vowelConsonantCount(string):
    #accumulator
    consCount = 0
    #accumulator
    vowelCount = 0
    #loop thru input string
    for letter in string:
        #check if vowel
        if vowelChecker(letter):
            #add if vowel
            vowelCount += 1
            #return to top
            continue
        #add if not vowel
        consCount += 1

    #return array of vowelCount and consCount
    return ["Vowel: " + str(vowelCount), "Consonants: " + str(consCount)]

#entrance point
main()