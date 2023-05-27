ope = open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/fibbo.py","r")
with open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/fibbo.py") as opeg: 
    op = open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/new.txt","w")
    count = 0
    for lines in opeg:
        countOfChar = 0
        for words in lines:
            countOfChar += 1
        count +=1
        op.write(f"Line {count} contains {countOfChar} count of words \n")
    op.write(f"\ntotal Lines = {count}")
ope.close()
op.close()