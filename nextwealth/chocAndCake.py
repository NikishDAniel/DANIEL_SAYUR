#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.

#find how many choc and cake the user can buy

noOfCake = 0
noOfChoc = 0
#get budget
#FillinMissingCode
money = float(input("Enter the budget : "))
while (money >= 150) : 
    if (money >= 200) :
        #buy choc
        noOfChoc += 1
        money -= 200
    elif (money >= 150):
        noOfCake += 1
        money -= 150
    
    #FillinMissingCode for buying cake


#print no of cakes and choc
print(f'number of cakes bougth {noOfCake} and number of choc bought {noOfChoc}')
#FillinMissingCode