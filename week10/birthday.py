'''friends invite and food order '''
'''
def friendsInvitation(number,color,place):
    for i in range(number):
        name = input()
        print(f'{color} color invitation . My dear friend {name} here is the invitation to my birthday party!  place : {place}')
        
def foodOrder(food,budget,number):
    print(f"You have ordered {food} for {number} persons within the budget of {budget}")
        
foodOrder("Sambar satham",1000,25)
friendsInvitation(5,"Black","madurai")
'''
def sum (number1,number2):
    sumOfTwo = number1+number2
    return sumOfTwo
output = sum(int(input()),int(input()))
print("The sum of two numbers is :",output)