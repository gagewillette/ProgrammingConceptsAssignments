def writeScores():
    name = ""
    score = ""
    namesAndScores = []
    while True:
        try:
            name = input("Input player name or type \"EXIT\": ")
            if name == "EXIT":
                break
            score = int(input(f"Input score for player, {name}: "))
            namesAndScores.append(f"{name}: {score} \n")
        except ValueError:
            print("You must input an integer!")
            continue
    f = open("golf.txt" , 'w')
    f.writelines(namesAndScores)
    f.close()

    
def readScores():
    with open("golf.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(line)

writeScores()
readScores()