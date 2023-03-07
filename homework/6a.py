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
message = 'I Love India'
pattern = '*** **** ** **********     *****'

messageWithoutSpace = message.replace(' ','')
messagelength = len(messageWithoutSpace) -1
string=''
messageIndex = 0
for i in pattern:
    if i == '*':
        string += messageWithoutSpace[messageIndex]
        messageIndex +=1
        if messageIndex > messagelength:
            messageIndex =0
    else:
        string += i   
print(string)
