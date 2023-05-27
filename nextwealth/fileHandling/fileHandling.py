openFile = open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/fibbo.py","r")
with open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/fibbo.py") as opened: 
    newFile = open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/new.txt","w")
    count = 0
    for lines in opened:
        countOfChar = 0
        for words in lines:
            countOfChar += 1
        count +=1
        newFile.write(f"Line {count} contains {countOfChar} count of words \n")
    newFile.write(f"\ntotal Lines = {count}")
openFile.close()

newFile.close()