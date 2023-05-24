############## Problem 2 ####################
#Ask the user how many members in the family. Get Name, age and height and weight.
#add the details into four lists.
#Print the each memeber of the family and their details
#eg output 
# Name      Age     Height(cm)      Weight(kg)
# Ram       35      180             80
# Seetha    34      145             58
#
nameList = []
ageList = []
heightList = []
weightList = []
#FillinMissingCode for other data
noOfPeople = int (input("How many people in the family "))
for member in range (1, noOfPeople + 1):
    details = input(f"Enter the details of member {member} Name, age, height, weight ")
    #FillinMissingCode Split the input string and add it to the lists
    detailsList = details.split()
    nameList.append(detailsList[0])
    ageList.append(detailsList[1])
    heightList.append(detailsList[2])
    weightList.append(detailsList[3])

#print the header 
print ("Name\t\tAge\t\tHeight(cm)\t\tWeight(kg)") #learn about \t
for index, member in enumerate(nameList): #Learn how enumerate works
    print( f"{member}\t\t{ageList[index]}\t\t{heightList[index]}\t\t\t{weightList[index]}")