'''plan 
    -- input two chances'''
    
def spare(totalRoll):
    oneChance = int(input())
    totalPoint = totalRoll + oneChance   
    return totalPoint
def twoRoll():
    first = int(input())
    second = int(input())
    strike = first + second
    return strike
def strike(firstRoll):
    strikePoint = firstRoll
    total = twoRoll()
    totalPoint = strikePoint + total  
    return totalPoint
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
            return totalPoint
        elif totalRoll < 10:
            totalPoint = totalRoll
            return totalPoint
        else:
            roll()
    else:
        print("Enter the correct value.")
    return totalPoint
    
def main():
    totalPoints = 0
    for i in range(12):
        totalPoints +=roll()
    return totalPoints
output = main()
print(output)  