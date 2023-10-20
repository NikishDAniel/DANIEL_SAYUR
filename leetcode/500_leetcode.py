'''Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]'''

'''message = ["adsdf","sfd"]

def checkSameRow(string,strLen,length=0,prev=0):
    rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    index = [rows.index(x) for x in rows if string[length] in x][0]
    if length > 0 and index != prev:
        return False
    elif length == strLen-1:
        return True
    elif length < 1 or index == prev:
        return checkSameRow(string,strLen,length+1,prev=index)
print([i for i in message if checkSameRow(i.lower(),len(i)) == True])


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []

        for word in words:
            for r in rows:
                if len(word) == len([n for n in word.lower() if n in r]):
                    result.append(word)
        return result'''
    
def checkSameRow(string):
            rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
            for i in rows:
                if string in i:
                    return i
output = []
words = ["Hello","Alaska","Dad","Peace"]
for i in words:
    lowered = i.lower()
    row = checkSameRow(lowered[0])
    if len(i) == len([x for x in lowered if x in row]):
        output += [i]
print(output)