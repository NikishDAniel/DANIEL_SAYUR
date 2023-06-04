'''
Same details as above.
But the input is in a file in the following format

Name/Month  Sam    Adam     Sara
Month1      300     340     1000
Month2      567     456     234
Month3      234     456     3000
Month4      1000    234     2000   

Find the name of the employee who had the most the phone sales each month and add it to the end of the
table and write it back to the file

eg
Name/Month  Sam    Adam     Sara    MostSales
Month1      300     340     1000    Sara    
Month2      567     456     234     Sam    
Month3      234     456     3000    Sara
Month4      1000    234     2000    Sara


Also , print the employee who sold most phones in all 4 months added.

'''


filr = open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/nestedLoops2/sample.txt","r")
with open("C:/Users/Nikish daniel/Desktop/DANIEL_SAYUR/nextwealth/nestedLoops2/sample.txt") as opened:
    for line in opened:
        line = line.split()
        for i in range(len(line)):
            if i>0 and line[i].isalpha():
                
            elif i > 0 and line[i].isnumeric():
               
            else:
                continue