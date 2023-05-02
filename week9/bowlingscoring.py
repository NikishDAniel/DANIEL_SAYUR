'''plan 
    -- input two chances'''
# function to spare  
def spare(totalRoll):
    # in spare there is one roll chance 
    oneChance = int(input())
    # adding the spare points + chance points 
    totalPoint = totalRoll + oneChance 
    # returning the total spare point  
    return totalPoint

# a function to take two roll chances
def twoRoll():
    first = int(input())
    second = int(input())
    strike = first + second
    # returning the total strike point  
    return strike

# a function to strike 
def strike(firstRoll):
    strikePoint = firstRoll
    # a function call to tworoll function
    total = twoRoll()
    totalStrikePoint = strikePoint + total  
    return totalStrikePoint
def roll(): 
    totalPoint = 0
    firstRoll = int(input()) 
    if firstRoll == 10:
        totalPoint = strike(firstRoll)
        
    elif firstRoll < 10:
        secondRoll = int(input())
        totalRoll = firstRoll+secondRoll
        if totalRoll == 10:
            totalPoint = spare(totalRoll)
        elif totalRoll < 10:
            totalPoint = totalRoll
        else:
            roll()
    else:
        print("Enter the correct value.")
    return totalPoint
    
def main():
    totalPoints = 0
    for i in range(10):
        totalPoints +=roll()
    return totalPoints
output = main()
print(output)  