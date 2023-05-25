############## Problem 2 ####################
#Ask the user how many members in the family. Get Name, age and height and weight.
#add the details into four lists.
#Print the each memeber of the family and their details
#eg output 
# Name      Age     Height(cm)      Weight(kg)
# Ram       35      180             80
# Seetha    34      145             58
#


# create a empty list that contains information  
nameList = []
ageList = []
heightList = []
weightList = []
noOfPeople = int (input("How many people in the family "))

# looping for the members in the family
for member in range (1, noOfPeople + 1):
    details = input(f"Enter the details of member {member}  -->  Name, age, height, weight ")
    #FillinMissingCode Split the input string and add it to the lists
    detailsList = details.split()
    nameList.append(detailsList[0])
    ageList.append(detailsList[1])
    heightList.append(detailsList[2])
    weightList.append(detailsList[3])

#printing the header 
print ("Name\t\tAge\t\tHeight(cm)\t\tWeight(kg)") 

# loop that takes and print the details
for index, member in enumerate(nameList): 
    print( f"{member}\t\t{ageList[index]}\t\t{heightList[index]}\t\t\t{weightList[index]}")
    
'''
output --
How many people in the family 3
Enter the details of member 1  -->  Name, age, height, weight  daniel 20 165 63
Enter the details of member 2  -->  Name, age, height, weight  Ram       35      180             80
Enter the details of member 3  -->  Name, age, height, weight Seetha    34      145             58
Name            Age             Height(cm)              Weight(kg)
daniel          20              165                     63        
Ram             35              180                     80        
Seetha          34              145                     58  

'''