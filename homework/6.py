'''6. Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "*** **** ** **********     *****"
      Output  - "ILo veIn di aILoveIndi     aILov"

     Note how you replace each * in the pattern with the letter in the message, the space in the message doesn't
     matter, but the space(s) in the pattern matters.'''

'''plan:
    1. getting string and pattern
    2. removing space in the string
    3. '''



message = 'I Love India' #input("Enter the message  :")
messageWithoutSpace = message.replace(' ','')
pattern = '*** **** ** **********     *****' #input ("Enter the pattern :")
length = len(messageWithoutSpace)
string = ''


for i in pattern:
    string += messageWithoutSpace[i]
    print(string)