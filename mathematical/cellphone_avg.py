'''2.Write an app for a phone sales man. The Salesman earns Rs10000 every month.
 He earns Rs1000 commission for every phone he sells. If he sells more than 5 phones a month,
  he earns extra Rs100 per phone (1000+100). If he sells 10 phones or more, 
  he gets extra Rs 200 for each phone over 10. He can only earn max 25000 per month. He gets a bonus of Rs 25000 per year
  if he sells more than 100 phones in a year. 
   Calculate his monthly salary and avg salary per month in one year.'''

# assigning the initial values
monthly_salary = 10000
max_month=25000
salary_per_month=0
salary=0
commission = 1000
phones_5_to_9=100
phones_10_and_greater=100
year_bonus = 25000
avg_salary = 0

# created a empty list for that we can show the number of phones sold per month
phone=[]

# create a loop because we need to run the same code for 12 times for completing the year 
for i in range (1,13):
    print(f"Month {i} :")  # this line is to print month
    no_of_phones_sold_per_month = int(input(f"Enter the number of phones sold in month {i} :"))   # getting input from the user
    phone.append(no_of_phones_sold_per_month)      #this is append function to add the number of phones in the list
    if no_of_phones_sold_per_month == 0 :          # before doing operations we need to check whether the number of phones sold is equal to zero
        salary_per_month=monthly_salary
    elif ( no_of_phones_sold_per_month >= 5 or no_of_phones_sold_per_month < 10 ):   
        print(f"You sold {no_of_phones_sold_per_month} phones. You'll get {phones_5_to_9} extra per phone.")
        salary_per_month=no_of_phones_sold_per_month*(1000 + 100)+monthly_salary
    elif no_of_phones_sold_per_month >= 10:
        print(f"You sold {no_of_phones_sold_per_month} phones. You'll get {phones_10_and_greater} extra per phone.")
        salary_per_month=no_of_phones_sold_per_month*(1000 + 200)+monthly_salary
    if max_month > salary_per_month :
        print("Your salary is : ", salary_per_month)
    elif max_month < salary_per_month:
        print(f"Your salary is {salary_per_month} which is greater than 25000.")
      
    total_phones_per_year=sum(phone)        #this to calculate the total phones
    print("Total phones sold per year :",total_phones_per_year)     
    if total_phones_per_year > 100:
        salary=salary+year_bonus
print(phone) 
print("Average salary =" , salary/12)