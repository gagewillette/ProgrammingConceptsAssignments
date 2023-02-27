# writeScores() asks the user for input [Name, Score] and writes it to a txt file 
# readScores() opens the txt file and print each player and their score

#define func
def writeScores():
    #intialize variables & array
    name = ""
    score = ""
    namesAndScores = []
    #open infinite loop
    while True:
        #open try/catch
        try:
            #accpet name input 
            name = input("Input player name or type \"EXIT\": ")
            #add break for loop
            if name == "EXIT":
                break
            #get player score
            score = int(input(f"Input score for player, {name}: "))
            #add name and scores to array
            namesAndScores.append(f"{name}: {score} \n")
        #catch and non-integer inputs
        except ValueError:
            print("You must input an integer!")
            continue
    #open file as write    
    f = open("golf.txt" , 'w')
    #write data to file
    f.writelines(namesAndScores)
    #close file writer
    f.close()

#define func
def readScores():
    #open file as read
    with open("golf.txt" , 'r') as f:
        #read lines
        lines = f.readlines()
        #iterate through each line & print
        for line in lines:
            print(line)


#call funcs
writeScores()
readScores()