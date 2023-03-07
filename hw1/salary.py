'''4. Calcualte the salary of the phone salesman for a month. His monthly salary is Rs10000. If he sells a phone for 
Rs 15000 or more, he gets Rs1000 commission per phone. If sells a phone for Rs40000 or more, he gets Rs2000 per phone in commision.'''

monthly_salary = 10000
commission_1=1000
commission_2=2000
hike=0
no_of_phone_sold = int(input("Enter the number of phones you sold :"))
if no_of_phone_sold == 0:
    print("Your salary : ", monthly_salary)
for i in range(1,no_of_phone_sold+1):
    phone=int(input("Enter the amount you sold per phone :"))
    if phone <15000 :
        print(f"Your salary is {monthly_salary}")
    elif (phone >=15000 and phone < 40000) :
        hike+=commission_1
        print(hike)
    elif (phone >=40000):
        hike+=commission_2
        print(hike)
salary=monthly_salary+hike
print("Your salary is ", salary)
    