'''Count the number of each chars in a string. Use Dictionary.
 Print the chars and its num of occurrence in the same order as it appears in the string'''

message = "We Attack at Dawn"
message = message.lower()
messageWithoutSpace = message.replace(" ","")
dict = {}
new =''
print(messageWithoutSpace)
for keys in messageWithoutSpace:
    countOfSame = messageWithoutSpace.count(keys)
    if keys not in new:
        #countOfSame = messageWithoutSpace.count(keys)
        print(f'count of {keys}: {countOfSame}')
        new = new+keys
    dict.update({keys:countOfSame})
print(dict)