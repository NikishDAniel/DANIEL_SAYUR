''' 1. In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
  Use functions.
'''
'''
    -- define a main function that takes input.
    -- '''
def next(character):
    newCharacter = ord(character)
    newCharacter = chr(newCharacter + 1)
    return newCharacter

#defining the main function
def main(message,character):
    index1 = message.find(character)
    if message.find(character) == -1:
        next(character)
        character = next(character)
        main(message,character)
    #checking for the character is present
    elif message.find(character) != -1:
        index2 = message.rfind(character)
        print(f"{character} is found in {index2}")
        #if both the index values are same we are going to take next character
        if index2 == index1:
            print(f"There is no 2nd {character} in the {message}")            
            newCharacter = next(character)
            main(message,newCharacter)
        #if index2 equals index1 value+1 then
        elif index2 == index1+1:
            print(f"Both the letters are placed followed by each other")
        elif index1 != index2:
            result = slice(index1+1,index2)
            print(message[result])           
#main function call
main(message = input(),character = input())
'''
a = ord('A')
print(chr(a+1))
'''