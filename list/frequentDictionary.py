'''Count the number of each chars in a string. Use Dictionary.
 Print the chars and its num of occurrence in the same order as it appears in the string'''

message = input("Enter a character :")#"We Attack at Dawn"
message = message.lower()
messageWithoutSpace = message.replace(" ","")
dict = {}
string =''
newString =''
print(messageWithoutSpace)
for keys in messageWithoutSpace:
    countOfSame = messageWithoutSpace.count(keys)
    if keys not in newString:
        print(f'count of {keys}: {countOfSame}')
        newString = newString+keys
    dict.update({keys:countOfSame})
print(dict)
for key,ele in dict.items():
    h = key,ele
    string += str(h)
    string = string.replace("(","")
    string = string.replace(" ","")
    string = string.replace("'","")
    string = string.replace(",","")
    string = string.replace(")","")
print(string)