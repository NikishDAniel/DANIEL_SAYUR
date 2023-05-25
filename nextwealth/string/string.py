########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g

# getting input
inputString = input("Enter the string : ")
i = 0 #counter to track the chars
newString = ""

# looping through the characters
while i < len(inputString):
    newString += inputString[i:i+2]
    newString += " " #add space
    i+=2
print (newString)


'''output 1 --
Enter the string : abcdefg
ab cd ef g 

'''

'''
output 2 --
Enter the string : daniel
da ni el

'''