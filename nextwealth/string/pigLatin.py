########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = input("Enter the input string : ")
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']

for word in inputSentence.split(): #gets the word in a sentence
    #take the first chars until a vowel
    first_vowel_index = 0
    #FillinMissingCode - check if the word has more than one char
    if len(word)==1:
        words = word[0]+pigLatinKey
    else:
        words = ''
        for index, char in enumerate(word): #returns both the index and the char in the word
            if char not in vowels:
                if len(word)==index+1:
                    pass 
                else:   
                    words += char
                            
            else: 
                first = word[index+1]              
                words = first + words[0:]+char+pigLatinKey
         #FillinMissingCode - check if the char is vowel or not
        #
    print(words,end=' ')