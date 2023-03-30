''' 1. In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
  Use functions.
  2. Extension of Cafe  
    2.1Replenish supply for every 5 customers  and at the end of the day

    2.2 Calculate replenish supply at the starting of the day for hot items, every 5 customers for all items and only cold items  at the every end of the day.'''
#getting input
message = input()
i=0
m = ''
if message[i] == "A":
  m = message.split(message[i])
  
else:
  i +=1 
sa = m[1]
print(sa)
if ("A" in sa )or ("B"in sa )or ("C"in sa):
  print(sa)
