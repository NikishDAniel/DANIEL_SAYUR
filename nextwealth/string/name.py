########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

# getting input
myName = input("My name : ")
output = ''
#looping through the name
for letter in myName:
    output += letter
    print(output)
    
'''output --
My name : Daniel
D
Da
Dan
Dani
Danie
Daniel'''  