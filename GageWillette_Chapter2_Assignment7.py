#   A car’s miles-per-gallon (MPG) can be calculated with the following formula:
#   MPG = Miles driven /  Gallons of gas used
#   Write a program that asks the user for the number of miles driven and the gallons of gas used. It should calculate the car’s MPG and display the result.
#
#   the follwing program will ask the user for input (mpg and gallons used.
#   on correct input, the program will calculate MPG and dispaly it to the user


#instantiate variable for later use
MilesDriven = 0

#instantiate variable for later use
GallonsUsed = 0

#instnaite variable for later use
FinalMPG = 0

#create infinite event loop
while True:
    #run code below and catch any compilation errors
    try: 
        #take integer specific input as assign to variable
        MilesDriven = int(input("How many miles did you drive?:  "))
        #take integer specific input as assign to variable
        GallonsUsed = int(input("How many gallons of gas did you use?:  "))
        #break infinite loop if no errors are thrown
        break
    #catch any thrown errors
    except ValueError:
            #notify user of invalid input
            print("Please input a integer value!")
            #restart loop
            continue

#assign previously instaniated variable to final computation using inputs
FinalMPG = MilesDriven / GallonsUsed

#check if MPG is over 15
if FinalMPG > 15:
    #fianl output
    print("Your MPG was " + str(FinalMPG) + ", not bad!")
#run if first condition is not met
else:
    #fianl output
    print("Your MPG was " + str(FinalMPG) + ", that's gonna be expensive!")

