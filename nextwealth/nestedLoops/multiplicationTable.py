######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

'''   1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25'''

# a function to print first row of x
def printX():
  for i in range(startNumber,endNumber+1):
      print(f'\t{i}',end=" ")
  print()
  print(f"**********"*i)

startNumber = int(input("Enter the starting number : "))
endNumber = int(input("Enter the ending number : "))
for i in range(2):
  if i == 0:
    printX()
  else:
    for i in range(startNumber,endNumber+1):
        for j in range(startNumber,endNumber+1):
            mul = i*j
            if j== startNumber:
                print(f'{i} |\t{mul}',end = ' ')
            else:
                print(f'\t{mul}',end = ' ')
        print()


'''
output --
Enter the starting number : 1
Enter the ending number : 5
  1 2  3  4  5  
 *************************
1 | 1 2 3 4 5
2 | 2 4 6 8 10
3 | 3 6 9 12 15
4 | 4 8 12 16 20
5 | 5 10 15 20 25

'''

'''output 2 ---
Enter the starting number : 5
Enter the ending number : 8
    5 6  7  8  
 *******************************
5 | 25 30 35 40
6 | 30 36 42 48
7 | 35 42 49 56
8 | 40 48 56 64

'''