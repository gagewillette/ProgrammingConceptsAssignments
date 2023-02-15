#the follow program will accept how fast one was going and for how long
#the program will then display to the user on each hour, how far they have travelled to that point

#initalize variables and get input
totalSpeed = int(input("How fast were you travelling on your trip? (MPH): "))
totalDistance = int(input(f"How far did you travel at {totalSpeed}MPH? (hours):"))

#start a loop with (value of toatlDistance) iterations
for i in range(1 , totalDistance + 1):
    #print, for each hour, the hour count and how far you have travelled at this point
    print(f"Hour: {i} Distance Travelled: {i * totalSpeed}")

