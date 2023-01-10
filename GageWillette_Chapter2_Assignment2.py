# the code below, on compile, accepts user input (represented as total sales)
# following this input, the total sales is converted into profit using a constant multiplier

# define a constant multiplier that is used for later computation
MULTIPLIER = .23

# create an infinite loop
while True:
    # try the code provided below and look out for errors
    try:
        # assign "totalsales" to the integer value that is provided by the user
        totalsales = int(input("Please enter total sales: "))
        # break the loop if no errors are thrown (input is correct)
        break
    # catch a value error that can be raised from the user inputting a string value
    except ValueError:
        # inform the user that they inputted an incorrect value
        print("Please input a number (integer value only)")
        # return to top of event loop to allow for correct inputs
        continue

# take 23 percent of the profits provided in input
profits = totalsales * MULTIPLIER

# display total profits to the console
print("The total profits are: " + str(profits))
