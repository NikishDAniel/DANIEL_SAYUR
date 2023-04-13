'''
Write a Python program that iterates the integers from 1 to 50.
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
For numbers that are multiples of three and five, print "FizzBuzz".
'''
'''
    -- define a function that takes no arguments and it contains local variables to hold 'fizz' 'buzz' and 'fizzbuzz'
    -- looping to the same with respect to some conditions
    -- set global variable with string datatype
    -- return the finalstring'''
finalString = ''
def find():
    fizz = "Fizz "
    buzz= "Buzz "
    both = "FizzBuzz "
    for i in range(1,51):
        global finalString
        if (i %3 == 0 and i % 5 == 0):
            finalString += both 
        elif i % 5 == 0:
            finalString += buzz
        elif i %3 == 0:
            finalString += fizz
    return finalString
output = find()
print(output)
