########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = input("Enter the input string : ")
pigLatinKey = 'ay'
for word in inputSentence.split(): #gets the word in a sentence
    #take the first char
    firstChar = word[0]
    if len(word)==1:
        word = word[0]+pigLatinKey
    else:
        word = word[1:] + firstChar + pigLatinKey
    print(word,end = ' ')
        
'''output -- 

Enter the input string : I am Python
Iay maay ythonPay

'''