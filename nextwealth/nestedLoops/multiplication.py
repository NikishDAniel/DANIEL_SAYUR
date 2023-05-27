######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.

#function to return the multiplicated value
def multiplication(number1,number2):
  answer = number1*number2
  print(f'{number1} x {number2} = {answer}')

# getting input
number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))
numberOfRows = int(input("Enter the row number :"))

# looping through the each number 1 and number 2
for num1 in range(number1,number2+1):
  for num2 in range(1,numberOfRows+1):
    multiplication(num1,num2)
  print(end="-------------------\n")
  
'''
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
7 x 11 = 77
7 x 12 = 84
-------------------
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
8 x 11 = 88
8 x 12 = 96
-------------------
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
9 x 11 = 99
9 x 12 = 108
-------------------
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100
10 x 11 = 110
10 x 12 = 120
-------------------
11 x 1 = 11
11 x 2 = 22
11 x 3 = 33
11 x 4 = 44
11 x 5 = 55
11 x 6 = 66
11 x 7 = 77
11 x 8 = 88
11 x 9 = 99
11 x 10 = 110
11 x 11 = 121
11 x 12 = 132
-------------------
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
12 x 11 = 132
12 x 12 = 144
-------------------
13 x 1 = 13
13 x 2 = 26
13 x 3 = 39
13 x 4 = 52
13 x 5 = 65
13 x 6 = 78
13 x 7 = 91
13 x 8 = 104
13 x 9 = 117
13 x 10 = 130
13 x 11 = 143
13 x 12 = 156
-------------------
14 x 1 = 14
14 x 2 = 28
14 x 3 = 42
14 x 4 = 56
14 x 5 = 70
14 x 6 = 84
14 x 7 = 98
14 x 8 = 112
14 x 9 = 126
14 x 10 = 140
14 x 11 = 154
14 x 12 = 168
-------------------
15 x 1 = 15
15 x 2 = 30
15 x 3 = 45
15 x 4 = 60
15 x 5 = 75
15 x 6 = 90
15 x 7 = 105
15 x 8 = 120
15 x 9 = 135
15 x 10 = 150
15 x 11 = 165
15 x 12 = 180
-------------------
16 x 1 = 16
16 x 2 = 32
16 x 3 = 48
16 x 4 = 64
16 x 5 = 80
16 x 6 = 96
16 x 7 = 112
16 x 8 = 128
16 x 9 = 144
16 x 10 = 160
16 x 11 = 176
16 x 12 = 192
-------------------
'''



'''
output 2 --
Enter the first number : 5
Enter the second number : 5
Enter the row number :12
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
5 x 11 = 55
5 x 12 = 60
-------------------'''



'''
output 3 ---
Enter the first number : 1
Enter the second number : 3
Enter the row number :3
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
-------------------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
-------------------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
-------------------'''
