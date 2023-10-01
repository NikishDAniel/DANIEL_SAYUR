'''2. You are writing an essay. You don't want the any word to appear very frequently. Write a program that will
take your essay as input (maybe from a file) and print the number of times each unique word appears in your essay.'''

essay = input().replace(' ','').lower()
dict1 = {}
for i in essay:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1
print(dict1)