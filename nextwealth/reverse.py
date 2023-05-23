'''#def reverseString(message):
message = "Hello World !"
new = ''
message = message.split()
for words in message:
    first = words[0]
    last = words[len(words)-1]
    new = last + words[1:len(words)-1]+first
new += new
print(new)'''

ope = open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/fibbo.py","w")
ope.write("new line added")
ope.close()
ope = open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/fibbo.py","r")
print(ope.read())
'''Write a Python program to count the number of lines in a text file.
Write a Python program to count the frequency of words in a file.
the- 10'''