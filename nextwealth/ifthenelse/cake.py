########## Problem 3 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.
#find how many choc and cake the user can buy.


#initialise the variables
choc = 200
cake = 150
noOfChock , noOfCake = 0 , 0
stockOfChoc , stockOfCake = int(input("Number of choc the shop have : ")), int(input("Number of cake the shop have : "))
money = float(input("Enter the budget : "))

# loops until the money decreases than 150
while (money >= 150):
    if (money >= 150):
        stockOfCake -= 1
        money -= 150
        noOfCake += 1
    if (money >= 200) :
        stockOfChoc -= 1
        money -= 200
        noOfChock += 1
    
print(f'The users can bought {noOfChock} number of choc and {noOfCake} numbers of cake')    

'''
output --
Number of choc the shop have : 45
Number of cake the shop have : 50
Enter the budget : 1500
The users can bought 4 number of choc and 4 numbers of cake

'''