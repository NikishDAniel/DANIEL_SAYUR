'''
Write a Python program that iterates the integers from 1 to 50.
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
For numbers that are multiples of three and five, print "FizzBuzz".
'''
'''
    -- define three functions to check if any condition is true
    -- looping to the same with respect to some conditions
    -- return values'''

#multiple of 5 function
def multiple5(i):
    if i%5 == 0:
        return "Buzz"
    else:
        return i
    
# multiple of 3 function
def multiple3(i):
    if i%3 == 0:
        return "Fizz"
    else:
        mul =multiple5(i)
        return mul
# frist of all need to check for both multiples   
def both(i):
    if (i %3 == 0 and i % 5 == 0):
        return "FizzBuzz"
    else:
        mul = multiple3(i)
        return mul
    
#here is the main function
def main():
    for i in range(1,51):
        print(both(i))

main() 