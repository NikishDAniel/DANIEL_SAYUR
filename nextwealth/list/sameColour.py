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
# looping until the loop breaks
while(True):
    print("Friend 2")
    colour = input("Enter your favourite colour : ")
    # if the colours not in the list then appending it in other list
    if colour not in coloursList:
        outputList.append(colour)
        print("Try again")
    else:
        print(f'You both like {colour}')
        attempts += 1
        
    # if the attempts finished then break the loop
    if attempts == 3:
        break
    
print(outputList) 

'''
output 1 --
Friend 1
Enter your favourite colors : red green blue black white pink sandal
Friend 2
Enter your favourite colour : grey
Try again
Friend 2
Enter your favourite colour : red
You both like red
Friend 2
Enter your favourite colour : purple
Try again
Friend 2
Enter your favourite colour : green
You both like green
Friend 2
Enter your favourite colour : blue
You both like blue
['grey', 'purple']
'''      


'''output 2 ---
Friend 1
Enter your favourite colors : red green blue black white pink sandal
Friend 2
Enter your favourite colour : red
You both like red
Friend 2
Enter your favourite colour : green
You both like green
Friend 2
Enter your favourite colour : black
You both like black
[]
'''