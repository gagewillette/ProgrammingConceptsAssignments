# the following program accepts user input corresponding
# to the two side lengths (length & width). after input
# the program with determine the areas of the rectangles
# and output the greater of the two

#init variables & set to null
lengthOne = None
widthOne = None
lengthTwo = None
widthTwo = None

# for later use
areaOne = None
areaTwo = None

#create infinite event loop
while True:
    #try this code
    try:
        # get the measurements for all 4 arguments
        lengthOne = int(input("Input first length (int only): "))
        widthOne = int(input("Input first width (int only): "))
        lengthTwo = int(input("Input second length (int only): "))
        widthTwo = int(input("Input second width (int only): "))
        #break loop if no issues
        break
    # run this if error
    except ValueError:
        print("Please input integer values!")
        #restart loop
        continue

#compute both areas for later comparison
areaOne = lengthOne * widthOne
areaTwo = lengthTwo * widthTwo

print("debug: " , areaOne , " " , areaTwo)

#check if areaOne is larger than areaTwo
if areaOne > areaTwo:
    #computer difference between areaOne and areaTwo
    diff = areaOne - areaTwo
    #let user know areaOne is larger
    print(f"The first rect is bigger than the second by {diff} units!")
# run if first condition is not met
elif areaTwo > areaOne:
    #compute difference between areaTwo and areaOne
    diff = areaTwo - areaOne
    #let user know areaTwo is larger
    print(f"The second rect is bigger than the first by {diff} units!")
else:
    print("The areas are the same!")
