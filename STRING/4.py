'''4. Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd. 
 ac2acc#cd3 acaccdcdcd'''

# using functions to decrypt the string

def decrypt(string):
    sDecrypt = ''
    sub = ''
    listSpecial = ['`','~','!','@','#','$','%','^','&','*','-','_','+','?']
    for i in string:
        if i.isalpha():
            sub += i
        if i.isdigit():
            sub *= int (i)
            sDecrypt += sub
            sub=''
        if i in listSpecial:
            string=string.replace(i,'')
            
    print(sDecrypt)
    print(len(sDecrypt))
strEncrypted = input("Enter encrypted string :")
strDecrypted = decrypt(strEncrypted)
