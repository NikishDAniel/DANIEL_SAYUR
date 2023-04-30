'''Write a Python function that accepts a string and counts the number of upper and lower case letters.'''
''' -- input - string 
    -- output - number of uppercase aand lower case letters
    -- need functions to 1. takes input and take the spaces from the input string
                         2. to find the order of the string and to find the range 
                         3. to calculate the number of counts
'''

# initialize both counts equal to 0
upperCount = 0
lowerCount = 0
# this function is to calculate the number of counts
def countOf(returning):
    global upperCount,lowerCount
    if returning is True:
        upperCount += 1
    elif returning is False:
        lowerCount += 1
# this function is to return whether true or false based on the condition
def check(i):
    if i.isupper():
        return True
    elif i.islower():
        return False
# this is the main function that takes input and calls other functions
def main(message):
    string = message.replace(" ","")
    for i in string:
        returning = check(i)
        countOf(returning)
# function call to main function   
main(input("Enter the input string: "))
# printing both the values
print("Upper case letters count :",upperCount)
print("Lower case letters count :",lowerCount)