############## Problem  1 #################### 
#Ask first friend the colors they like. Save it in a list
#Ask another friend the same question. If the color is in the first friend's list, 
#Print "You both like "name of the color"
#If it is not in the first friend's list, Save it another list.
print("Friend 1")
colours = input("Enter your favourite colors : ")
coloursList = colours.split()
outputList = []
attempts = 0
while(True):
    print("Friend 2")
    colour = input("Enter your favourite colour : ")
    if colour not in coloursList:
        outputList.append(colour)
        print("Try again")
    else:
        print(f'You both like {colour}')
        attempts += 1
    if attempts == 3:
        break
print(outputList)       