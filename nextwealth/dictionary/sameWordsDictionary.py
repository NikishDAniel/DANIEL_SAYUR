########## Program 1
#find the list unique words in a sentence
#hint - Each word is a key, count is the value

sentence = "This is a cat and it has a tail and two eyes".replace(" ",'')
visited = []
sameDict = {}

for word in sentence:
    if word not in visited:
       visited.append(word)
    else:    
        if word not in sameDict:
            values = 0  
            sameDict[word] = values
        else:
            values = sameDict[word] 
        values = values + 1
        sameDict[word] = values
for keys in sameDict:
    print(f'The same word {keys} occurs {sameDict[keys]+1} times.')
    
    
'''    
output -- 

The same word i occurs 4 times.
The same word s occurs 4 times.
The same word a occurs 7 times.
The same word t occurs 4 times.
The same word h occurs 2 times.
The same word n occurs 2 times.
The same word d occurs 2 times.
The same word e occurs 2 times.
'''
########## Program 2

########## Program 1
#find the list unique words in a sentence
#hint - Each word is a key, count is the value

sentence = "This is a cat and it has a tail and two eyes".replace(" ",'')
visited = ""
sameDict = {}

for word in sentence:
    if word not in visited:
       visited += word
    else:    
        if word not in sameDict:
            sameCharactersCount = 0  
            sameDict[word] = sameCharactersCount
        else:
            sameCharactersCount = sameDict[word] 
        sameCharactersCount = sameCharactersCount + 1
        sameDict[word] = sameCharactersCount
for keys in sameDict:
    print(f'The same word {keys} occurs {sameDict[keys]+1} times.')
    
    
'''

output--

The same word i occurs 4 times.
The same word s occurs 4 times.
The same word a occurs 7 times.
The same word t occurs 4 times.
The same word h occurs 2 times.
The same word n occurs 2 times.
The same word d occurs 2 times.
The same word e occurs 2 times.
'''