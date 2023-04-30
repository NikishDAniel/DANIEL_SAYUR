'''
assignment: define/implement classes for bowling problem
leetcode: reverse integer and longest palindrome substring

bowling game :
        -- first need to create a frame
                -- defining functions to take frames it loops from 1 to 11
                -- number of pins in first chance
                        -- checks if the first chance is strike -- then got 10 points bonus and 2 chance points
                                                                -- if both 2 chances is also strike then repeat the same as above
                                                                        -- before 
                        -- if the first chance is not strike  -- then we have second chance 
                                        *in this second chance -- if we got all pins down then we got 1 chance bonus a
                                                                -- if not then add first and second chance points
                        '''
def twoChance():
    firstRoll = int(input("Enter the first roll : "))
    secondRoll = int(input("Enter the second roll : "))
    strikePoint = firstRoll + secondRoll
    return strikePoint
def lastFrame():
    strike = 0
    firstRoll = int(input("Enter the first roll : "))
    if firstRoll == 10:
        strike += twoChance()
    rollPoints = strike + firstRoll
    return rollPoints
def main():
    rollPoints = 0
    for frames in range(1,11):
        if frames < 10:
            firstRoll = int(input("Enter the first roll : "))
            if firstRoll == 10:
                rollPoints += firstRoll 
            else:
                secondRoll = int(input("Enter the second roll : ")) 
                rollPoints += (firstRoll + secondRoll)
            print(f"Points in frame {frames} : ",rollPoints) 
        else:
            rollPoints += lastFrame()
            print(f"Points in frame {frames} : ",rollPoints)      
main()
#
