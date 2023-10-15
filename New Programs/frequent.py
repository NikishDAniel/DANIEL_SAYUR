'''2. You are writing an essay. You don't want the any word to appear very frequently. Write a program that will
take your essay as input (maybe from a file) and print the number of times each unique word appears in your essay.'''

# taking input message
essay = input().replace(' ','').lower()
dict1 = {}
#looping through the letters in essay
for i in essay:
    # if letter not in dictionary it will create key as that letter and value as 1 else it will increase count 
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1
print(dict1)
print(f'The most frequent letter in your Essay is " {max(dict1,key=lambda x:dict1[x])} " .')


# Method - 2
#essay = input().replace(' ','').lower()

# changing the essay message to set
essaySet = set(essay)
lettersCount = {x:essay.count(x) for x in essaySet}
print(lettersCount)
print(f'The most frequent letter in your Essay is " {max(lettersCount,key=lambda x:dict1[x])} " .')