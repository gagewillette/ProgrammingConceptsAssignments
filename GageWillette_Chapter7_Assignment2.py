#this program generates 7 random numbers and them outputs them to the console

import random

#define main func
def main():
    #init num array
    randNums = []
    
    #7 iteration for loop
    for i in range(7):
        #append random number to array
        randNums.append(random.randrange(1, 60))

    #return random num array
    return randNums

#define print func
def printNums(randNumArr):
    #init buffer string
    bufferString = ""
    
    #loop thru num array
    for i in randNumArr:
        #add number to array
        bufferString += str(i) + " "

    #print bufferstring
    print(bufferString)

printNums(main())