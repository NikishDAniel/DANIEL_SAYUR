'''
. Write an app for the following two player game. You have a 6 x 6 board. 
Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
who rolled the dice.
When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
The player who gets 5 points first wins the game
'''
import random
#initializing the values
rowNumber = 0 
colNumber = 0
scorePointP1 = 0
scorePointP2 = 0
#positionP1 = [0,0]
#positionP2 = [0,0]
#getting dice input from the players

while 1:
    if scorePointP1 == 5 or scorePointP2 == 5 :
        break
    diceInputRow1 = random.randrange(6)
    diceInputcolumn1 = random.randrange(6)
    #positionP1 = [diceInputRow1,diceInputcolumn1]
    print(f"the position for player 1 {diceInputRow1,diceInputcolumn1}")
    diceInputRow2 = random.randrange(6)
    diceInputcolumn2 = random.randrange(6)
    #positionP2 = [diceInputRow1,diceInputcolumn1]
    print(f"the position for player 2 {diceInputRow2,diceInputcolumn2}")
    diceDiffCol = abs(diceInputcolumn1 - diceInputcolumn2)
    diceDiffRow= abs(diceInputRow1 - diceInputRow2)
    if diceDiffCol == 0 and diceDiffRow ==0:
        scorePointP2 += 1
    elif diceDiffCol <= 1 or diceDiffRow <= 1:
        scorePointP1 += 1
print(f"Player 1 scores {scorePointP1}")  
print(f"Player 2 scores {scorePointP2}")   
if scorePointP1 == 5:
    print("User 1 is the winner!")
else:
    print("User 2 is the winner!")   
       