#the following program accepts user input for each of their monthly car expenses
#the program will then create a running sum of the values and then print the final

#initalize all variables to Null
loanPayment = None
insuranceCost = None
oilCost = None
tireCost = None
maintenanceCost = None

#define main
def main():
    #accept user input
    loanPayment = int(input("How much do you pay for your LOAN each month?: ")) 
    insuranceCost = int(input("How much do you pay for your INSURANCE each month?: ")) 
    oilCost = int(input("How much do you pay for your OIL each month?: "))
    tireCost = int(input("How much do you pay for your TIRES each month?: "))
    maintenanceCost = int(input("How much do you pay for your OTHER MAINTENANCE each month?: "))

    #intialize cost array that is passed to computation function
    costArray = [loanPayment, insuranceCost, oilCost, tireCost, maintenanceCost]

    #print value that is RETURNED from calcExpenses()
    print(calcExpenses(costArray))

#define calcExpenses
def calcExpenses(billArray):
    #initalize running sum
    totalCost = 0
    #start for loop for each elemetn in billArray[]
    for curCost in billArray:
        #add to running total
        totalCost += curCost

    #return f string to main()
    return f"You pay {totalCost} dollars each month for your car!"

#create entry point
if __name__ == "__main__":
    #run main()
    main()
