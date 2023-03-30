''' 1. In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
  Use functions.
'''
'''
Plan:
    -- input will be string
    -- define a function to  

'''
def findChar(inputString,letter):
    index1 = inputString.find(letter)
    index2 = inputString.rfind(letter)
    if index1 == index2:
        return False,-1,-1
    else:
        return True,index1,index2
    
def findLetterList(inputString):
    letterList = sorted(set(inputString))
    return letterList

letterFound = False    
def main():
    inputstring = input("Enter the string :")
    for letters in ['A','B','C']:
        result = findchar(inputstring,letter)
        if result[0] == True:



'''
'''