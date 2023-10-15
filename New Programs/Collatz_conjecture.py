'''1.Write a program for Collatz_conjecture.
Collatz_conjecture means -  start with the input number. 
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the resulting number until the answer is 1.Eg, input is 8
output 8, 4,2, 1
input is 9
output 9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1

Get two numbers as input. Print the number that has less number of steps to reach 1.

'''

# defining a function 
def collatz(number):
    #initializing a variable to get the steps 
    count = 0
    # loop until the number not equal to 1 
    while number!=1:
        # checking odd or even
        if number%2==0:
            number=int(number/2)
        else:
            number=(3*number)+1
        count+=1
        #print(number,end=' ')
    #print()
    return count

#taking input for the number of inputs 
n = int(input("Enter the number of inputs : "))
resultList = [collatz(int(input(f'Enter the number {i}: '))) for i in range(1,n+1)]
print(f'The number that has less number of steps to reach 1 is number ""{resultList.index(min(resultList))+1}"" input number..')