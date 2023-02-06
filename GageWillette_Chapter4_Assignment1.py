#this program will start a 5 iteration loop representing the five days
#that bugs were collected. for each day the program will ask the user how
#many bugs were collected on that day. the program will then display
#the final amount of bugs

#intialize the totalBugs variable
totalBugs = 0

# start a loop of 5 iterations
for i in range(0 , 5):
    #add day total to totalBugs
    totalBugs += int(input(f"How many bugs did you collect on day {i + 1}?: "))
    

#let user know how many bugs were collected 
print(f"You collected {totalBugs} bugs across the five days!")

