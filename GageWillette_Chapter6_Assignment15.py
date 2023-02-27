#this func will open a txt file, iterate through each line and print the value

#define function
def printNums():
    #open file and assign var
    with open("numbers.txt" , 'r') as f:
        #iterate thru lines
        for i in f.readlines():
            #print lines
            print(i)

#func call
printNums()