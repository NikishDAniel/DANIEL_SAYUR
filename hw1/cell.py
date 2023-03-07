'''5. Same as above. Calculate his annual salary. He gets a bonus of Rs 5000 at the end of the year,
 if he sells 20 phones or more in a year.'''

monthly_salary = 10000
commission_1=1000
commission_2=2000

hike=0
salary=0
no_of_phone_sold = int(input("Enter the number of phones you sold :"))
if no_of_phone_sold < 20 :
    bonus=0
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
    salary=monthly_salary+hike+bonus
else:
    bonus=5000
    for i in range(20,no_of_phone_sold+1):
        phone=int(input("Enter the amount you sold per phone :"))
        if phone <15000 :
            print(f"Your salary is {monthly_salary}")
        elif (phone >=15000 and phone < 40000) :
            hike+=commission_1
            print(hike)
        elif (phone >=40000):
            hike+=commission_2
            print(hike)
    salary=monthly_salary+hike+bonus
print("Your salary is ", salary)
        