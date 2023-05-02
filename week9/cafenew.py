import mysql.connector
f = mysql.connector.connect(
    host="localhost",
    user="nikishDaniel",
    password="3122003",
    database = 'cafe'
)
mycursor = f.cursor()
mycursor.execute("select*from cafe")
'''def showMenu():
    for i in mycursor:
        print(i[1])'''
    
customers = 10
while customers!= 0 :
    for i in mycursor:
        print(i[1])
    for i in range(customers):
        print(showMenu())
    
'''mycursor.execute("CREATE TABLE Fruit_Details (fruit_id INTEGER, name VARCHAR(255)
, color VARCHAR(255), cost DECIMAL(5,2), city VARCHAR(255))")'''