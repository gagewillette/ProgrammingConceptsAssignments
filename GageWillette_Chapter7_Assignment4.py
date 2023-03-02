#this program asks the user for 10 numbers and appoints them to an array
#the program will calculate the following: min, max, average, and sum
#the computations will be displayed to the console

#define sum func
def arraySum(arr):
    #init accumulator
    total = 0
    #iterate thru array
    for i in arr:
        #accumulate
        total += i
    #return accumluator
    return total

#define avg func
def arrayAvg(arr):
    #return average of array computation
    return sum(arr) / len(arr)

#defin min func
def arrayMin(arr):
    #calculate position of array min
    minPosition = arr.index(min(arr))
    #return elements of array at minPosition
    return arr[minPosition]

#define max func
def arrayMax(arr):
    #calculate position of array max
    maxPosition = arr.index(max(arr))
    #return element of array at maxPosition
    return arr[maxPosition]

#define main func
def main():
    #init num array
    numArray = []
    
    #10 iteration for loop
    for i in range(1 , 11):
        #init current variable in scope of loop
        cur = 0
        #try following code
        try:
            #accept user input
            cur = int(input(f"Please enter number ({i}): "))
            #append input to numArray
            numArray.append(cur)
        #catch ValueErrors
        except ValueError:
            #notify user of incorrect input
            print("Please ensure you are inputting integer values!")
            #reloop
            continue
    
    #print the computations done on the array
    print(f"Array Sum: {arraySum(numArray)} \n")
    print(f"Array Min: {arrayMin(numArray)} \n")
    print(f"Array Max: {arrayMax(numArray)} \n")
    print(f"Array Avg: {arrayAvg(numArray)} \n")

#run main
main()