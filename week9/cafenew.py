import mysql.connector
f = mysql.connector.connect(
    host="localhost",
    user="nikishDaniel",
    password="3122003",
    database = 'cafe'
)
mycursor = f.cursor()
mycursor.execute("select*from cafe")
for i in mycursor:
    print(i)
'''mycursor.execute("CREATE TABLE Fruit_Details (fruit_id INTEGER, name VARCHAR(255)
, color VARCHAR(255), cost DECIMAL(5,2), city VARCHAR(255))")'''