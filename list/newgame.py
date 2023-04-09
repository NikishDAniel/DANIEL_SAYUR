'''
1. Write an app for the following two player game. You have a 6 x 6 board. 
Users take turns rolling the dice twice. first roll is row no, second roll is col number. 
Mark the spot (row, col) as claimed by the userwho rolled the dice.
When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
The player who gets 5 points first wins the game
'''


'''
    -- checking for any user who reaches the 5 points first if the condition is true then break the loop
    -- getting input from the user1
    -- set user1 position
    -- getting input from the user2
    -- set user2 position 
    -- check if user1 position equals user2 position
    -- if equals : add 1 point to user2 
    -- else : check if the position of user2 is within 1 col/row of a claimed spot of the user1
            -- if it is true: add 1 point to user1
    -- '''
'''def user(position):
    row = position[0]
    column = position[1]    
    print("row :",row)
    print("column :",column)
user1Point = 0
user2Point = 0

def main(roll):
    position = roll.split(" ")
    user(position)
main()
while (user1Point < 5 ) and (user2Point < 5):
    user1position = input("Enter user 1 position :")'''
def checkEqual(pos1,pos2):
    if (pos1[0] == pos2[0]) and (pos1[1] == pos2[1]):
        return True
    
def checkWithin(pos1,pos2):
    if (abs(pos1[0] - pos2[0]) == 1 or abs(pos1[1] - pos2[1]) == 1):
        return True

def user(position):
    position = position.split(" ")    
    return position
user1Points = 0 
user2Points = 0
while 1:
    if (user1Points == 5 or user2Points == 5):
        break 
    user1position = input("Enter user1 position : ")
    pos1 = user(user1position)
    user2position = input("Enter user2 position : ")
    pos2 = user(user2position)
    chect = checkEqual(pos1,pos2)
    checkWith = checkWithin(pos1,pos2)
    if chect == True:
        user2Points += 1
    if checkWith == True:
        user1Points += 1
    print("User 1 :",user1Points)
    print("User 2 :",user2Points)
""" 
    if (abs (list1[0] - list2[0] )==1 ) and (abs(list1[0] - list2[0] )==1):"""