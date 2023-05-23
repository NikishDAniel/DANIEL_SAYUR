'''plan 
    -- input two chances
    -- funtions : strike , spare, two roll , roll , main
    '''
# spare function   
def spare(totalRoll):
    # in spare there is one roll chance 
    oneChance = int(input("Enter the number of pins knocked in spare option : "))
    # adding the spare points + chance points 
    totalPoint = totalRoll + oneChance 
    # returning the total spare point  
    return totalPoint

# a function to take two roll chances
def twoRoll():
    firstChance = int(input("Enter the number of pins knocked in first chance of strike : "))
    secondChance = int(input("Enter the number of pins knocked in second chance of strike : "))
    strike = firstChance + secondChance
    # returning the total strike point  
    return strike

# a function to strike 
def strike(firstRoll):
    strikePoint = firstRoll
    # a function call to tworoll function
    total = twoRoll()
    totalStrikePoint = strikePoint + total 
    # returning total strike points 
    return totalStrikePoint

# a function to roll 
def roll(): 
    totalPoint = 0
    firstRoll = int(input("Enter the first roll : ")) 
    # if first roll is 10 then it is Strike 
    if firstRoll == 10:
        # function call to strike
        totalPoint = strike(firstRoll)
    # if it is not strike then it will give second chance  
    elif firstRoll < 10:
        secondRoll = int(input("Enter the second roll : "))
        totalRollPoint = firstRoll+secondRoll
        # if first roll + second roll = 10 then it is Spare
        if totalRollPoint == 10:
            
            totalPoint = spare(totalRollPoint)
        # if it is > 10 it simply calculate the total point
        elif totalRollPoint < 10:
            totalPoint = totalRollPoint
        # if it is > 10 it will show wrong input message and takes first roll and so on
        else:
            print("Please enter the correct value.")
            roll()
    else:
        print("Please enter the correct value.")
    return totalPoint
# main function   
def main():
    finalTotalPoints = 0
    # looping for each frames
    for i in range(10):
        finalTotalPoints +=roll()
    return finalTotalPoints
output = main()
print(output)  
