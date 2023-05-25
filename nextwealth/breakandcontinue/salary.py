############## Problem  2 #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
# loop through each month
for month, phoneCount in enumerate(monthlySalesList):
    currentMonthSalary = 10000
    print (f"This month's salary before additional bonus {currentMonthSalary}") 
    # checking for bonus
    if (phoneCount >= 5):
        count = abs(phoneCount/5)
        bonus = count*5000
        # checking for phonecount greater than 5
        if (phoneCount > 5):
            count = phoneCount - 5
            bonus = count*1100
    # in first month there is no previous month salary
    if month == 0:
        previousMonthSalary = 0
    
    # if salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones he gets additional Rs5000.
    if (previousMonthSalary > 20000 or phoneCount >=20):
        currentMonthSalary += 5000 
        
    #else continue
    if(phoneCount < 20):
        previousMonthSalary = currentMonthSalary 
        continue 
    
    #calculate the new salary
    currentMonthSalary +=  bonus 
    print(f"This month's salary after additional bonus {currentMonthSalary}")
    previousMonthSalary = currentMonthSalary 
    
'''
output --
This month's salary before additional bonus 10000
This month's salary before additional bonus 10000
This month's salary after additional bonus 34800 
This month's salary before additional bonus 10000
This month's salary after additional bonus 32600 
This month's salary before additional bonus 10000
This month's salary before additional bonus 10000
This month's salary after additional bonus 34800 
This month's salary before additional bonus 10000
This month's salary before additional bonus 10000
This month's salary before additional bonus 10000
This month's salary before additional bonus 10000
This month's salary after additional bonus 33700 
This month's salary before additional bonus 10000
This month's salary after additional bonus 33700 
This month's salary before additional bonus 10000
This month's salary after additional bonus 46900
This month's salary before additional bonus 10000

'''