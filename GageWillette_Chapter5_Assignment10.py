#the following program accepts how many feet the user
#would like to convert. the input gets passed to 
# feet_to_inches() and returned back to main for output

#intialize variable
feet =  0
#initalize constant
INCHES_IN_FEET = 12

#define main()
def main():
    #accept user input and assign to feet
    feet = int(input("How many feet to convert to inches: "))
    
    #print final output
    print(f"{feet} conversts to {feet_to_inches(feet)} inches")

#def feet_to_inches() (helper function)
def feet_to_inches(feet):
    #return computation
    return feet * INCHES_IN_FEET

#create entry point
if __name__ == "__main__":
    #call main() func
    main()
    