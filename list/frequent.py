character = ''
characterDict = {}
character = character.lower()

while character != 'z':
    character = input("Enter a character:")
    if character in characterDict:
        characterDict[character] +=1
    else:
        characterDict[character] = 1

print(characterDict)