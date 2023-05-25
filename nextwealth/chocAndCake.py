#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.

#find how many choc and cake the user can buy

noOfCake = 0
noOfChoc = 0
#getting budget
money = float(input("Enter the budget : "))

# looping through the money 
while (money >= 150) : 
    if (money >= 200) :
        noOfChoc += 1
        money -= 200
    if (money >= 150):
        noOfCake += 1
        money -= 150
print(f'number of cakes bougth {noOfCake} and number of choc bought {noOfChoc}')


'''output 
Enter the budget : 1500
number of cakes bougth 4 and number of choc bought 4'''