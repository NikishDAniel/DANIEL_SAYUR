'''inputString = (input())
inputString =str(inputString)
reverse = ''.join(reversed(inputString)) 
if reverse == inputString:
    print("yes")'''
'''def printing():'''
    
# checkmatch function   
def checkmatch(inputString,i,firstLetter):
    # checks for the i value
    if i == 0:
        
        first = firstLetter
    else:
        first = inputString[i]
    last = inputString[(-i)-1]
    if first == last:
        return True
    else:
        return False
# main function
def main():
    # here i created a empty list to store the value at final stage
    resultList = []
    # getting input from the user 
    inputString = input("Enter the string : ")
    # taking the lenght of the string
    length = len(inputString)
    # taking the first letter from the input and changing them into lower case
    firstLetter = inputString[0].lower()
    # looping through the string
    for i in range(length):
        # checking if length is lesser or equal to the lenght of the string
        if i >= length:
            # if the above condition is true then it will break the loop
            break
        else:
            # else it goes to the function
            result = checkmatch(inputString,i,firstLetter)
            resultList.append(result)
            length -= 1
    
    if False in resultList:
        print("The given string is not a palindrome .")
    else:
        print("The given string is a palindrome .")
main()